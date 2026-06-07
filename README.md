# AIDefenseX

## AI-Based Intrusion Detection and Prevention System (IDPS)

AIDefenseX is an intelligent Intrusion Detection and Prevention System (IDPS) developed using Machine Learning, Wazuh SIEM, Suricata IDS/IPS, and Linux security tools. The system continuously monitors network traffic, detects malicious activities in real time, generates security alerts, and automatically responds to threats through IP blocking and active response mechanisms.

---

## Project Overview

Modern cyber attacks require rapid detection and automated response. AIDefenseX combines network-based intrusion detection, machine learning, security monitoring, and automated threat mitigation into a single solution.

The system collects network traffic logs from Suricata, analyzes them using a Python-based detection engine, generates alerts in Wazuh SIEM, and automatically responds to malicious activity using Linux firewall rules and Wazuh Active Response.

---

## Key Features

* Real-time network traffic monitoring
* Suricata IDS/IPS integration
* Wazuh SIEM integration
* Machine Learning based threat analysis
* Random Forest attack classification
* Automatic malicious IP blocking
* Wazuh Active Response integration
* Automatic malicious file removal
* Security alert generation
* Automated threat mitigation
* Linux-based deployment

---

## System Architecture

Attacker

↓

Network Traffic

↓

Suricata IDS

↓

eve.json Logs

↓

Python Detection Engine

↓

Machine Learning Analysis

↓

Wazuh SIEM Alert

↓

Active Response Engine

↓

iptables Auto Blocking / File Removal

↓

Threat Mitigated

---

## Technologies Used

### Security Tools

* Wazuh SIEM
* Suricata IDS/IPS
* iptables
* Linux Security Tools

### Programming

* Python

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* NumPy
* Pandas
* Joblib

### Operating System

* Ubuntu Linux

---

## Machine Learning Model

The machine learning component was trained using a Random Forest Classifier on CIC-IDS network traffic datasets.

Training Workflow:

1. Dataset Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Random Forest Training
6. Accuracy Evaluation
7. Model Serialization using Joblib

Model File:

* ids_model.pkl

Training Script:

* train_ids_model.py

---

## Dataset Information

Dataset Used:

* CIC-IDS Network Traffic Dataset

Dataset Statistics:

* Total Records Processed: 2,830,743+
* Features: 79
* Training Algorithm: Random Forest Classifier

---

## Performance Results

### Detection Accuracy

* Accuracy Achieved: 99.89%

### Threat Detection Capabilities

* Port Scanning Detection
* Flood Attack Detection
* Network Reconnaissance Detection
* Suspicious Traffic Analysis
* Unauthorized Access Attempts
* Real-Time Security Monitoring

---

## Automated Response Actions

The system automatically performs security actions when malicious activity is detected:

* Generates security alerts in Wazuh
* Blocks malicious IP addresses using iptables
* Triggers Wazuh Active Response
* Removes malicious or unauthorized files based on security rules
* Reduces response time to cyber threats

---

## Project Structure

AIDefenseX

├── code/

│ ├── ai_ids_detection.py

│ └── train_ids_model.py

├── model/

│ └── ids_model.pkl

├── docs/

│ ├── Wazuh_Architecture.png

│ └── Project_Report.pdf

├── screenshots/

├── requirements.txt

└── README.md

---

## Installation

Install Python dependencies:

pip install -r requirements.txt

Required Components:

* Wazuh SIEM
* Suricata IDS/IPS
* Ubuntu Linux
* Python 3.x

---

## Future Enhancements

* Threat Intelligence Integration
* Cloud Deployment
* Advanced Deep Learning Models
* SOC Dashboard Integration
* Automated Incident Response Workflows
* Multi-Host Threat Correlation

---

## Author

Rohan Kulkarni

Computer Engineering Student

Security Analyst Intern @ Error404 IT Solutions

Cybersecurity Enthusiast | Wazuh | Suricata | Python | Linux | Machine Learning

Email: [rohankulkarni7855@gmail.com](mailto:rohankulkarni7855@gmail.com)

LinkedIn: linkedin.com/in/rohan-kulkarni

---

## Disclaimer

This project was developed for cybersecurity research, educational purposes, and authorized security testing environments only. All testing should be performed on systems where proper authorization has been obtained.
