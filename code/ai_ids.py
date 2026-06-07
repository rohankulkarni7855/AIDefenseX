import json
import joblib
import time
import os
import subprocess
import warnings

warnings.filterwarnings("ignore")

# Load trained machine learning model
model = joblib.load("/home/rohan/ids_project/ids_model.pkl")

# Log file paths
logfile = "/var/log/suricata/eve.json"
alertfile = "/var/log/ai_ids.log"

# Dictionaries for tracking alerts and blocked IPs
last_alert = {}
blocked_ips = {}

# Configuration
COOLDOWN = 10      # Seconds between repeated alerts
BLOCK_TIME = 600   # Block duration in seconds

# Get victim machine IP address
victim_ip = subprocess.getoutput("hostname -I").split()[0]

print(f"AI IDS started. Monitoring victim IP: {victim_ip}")

with open(logfile, "r") as f:

    # Move to end of file and monitor new entries
    f.seek(0, 2)

    while True:

        current_time = time.time()

        # Remove expired IP blocks
        for ip in list(blocked_ips):
            if current_time - blocked_ips[ip] > BLOCK_TIME:
                os.system(f"sudo iptables -D INPUT -s {ip} -j DROP")
                print(f"UNBLOCKED: {ip}")
                del blocked_ips[ip]

        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        try:
            log = json.loads(line)

            # Process only flow events
            if log.get("event_type") != "flow":
                continue

            src_ip = log.get("src_ip", "")
            dest_ip = log.get("dest_ip", "")

            flow = log.get("flow", {})

            pkts_to_server = flow.get("pkts_toserver", 0)
            pkts_to_client = flow.get("pkts_toclient", 0)
            bytes_to_server = flow.get("bytes_toserver", 0)

            # Monitor only traffic related to victim machine
            if dest_ip != victim_ip and src_ip != victim_ip:
                continue

            # Identify attacker IP
            attacker_ip = src_ip if dest_ip == victim_ip else dest_ip

            # Ignore self traffic
            if attacker_ip == victim_ip:
                continue

            # Ignore localhost and invalid addresses
            if attacker_ip.startswith(("127.", "0.")):
                continue

            # Attack detection logic
            scan_detected = (
                pkts_to_server > 3 and pkts_to_client == 0
            )

            flood_detected = (
                pkts_to_server > 5 or bytes_to_server > 800
            )

            if not (scan_detected or flood_detected):
                continue

            now = time.time()

            # Generate alert after cooldown period
            if attacker_ip not in last_alert or now - last_alert[attacker_ip] > COOLDOWN:

                last_alert[attacker_ip] = now

                print(
                    f"ALERT: Attack detected from {attacker_ip} "
                    f"(Packets: {pkts_to_server})"
                )

                # Send alert to Wazuh
                with open(alertfile, "a") as a:
                    a.write(f"AI_IDS_ALERT {attacker_ip}\n")

                # Block attacker IP
                block_cmd = (
                    f"sudo iptables -C INPUT -s {attacker_ip} -j DROP "
                    f"2>/dev/null || "
                    f"sudo iptables -A INPUT -s {attacker_ip} -j DROP"
                )

                os.system(block_cmd)

                print(f"BLOCKED: {attacker_ip}")

                blocked_ips[attacker_ip] = time.time()

        except Exception:
            pass
