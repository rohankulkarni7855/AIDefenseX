import pandas as pd
import glob
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

files = glob.glob("*.csv")

df_list = []

for file in files:
    print("Loading:", file)

    data = pd.read_csv(file, low_memory=False)

    data.columns = data.columns.str.strip()

    data = data.replace([np.inf, -np.inf], 0)
    data = data.fillna(0)

    df_list.append(data)

print("Combining dataset...")

data = pd.concat(df_list, ignore_index=True)

print("Dataset shape:", data.shape)

X = data.drop("Label", axis=1)
y = data["Label"]

y = y.apply(lambda x: 0 if x == "BENIGN" else 1)

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Random Forest...")

model = RandomForestClassifier(n_estimators=50, n_jobs=-1)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "ids_model.pkl")

print("Model saved as ids_model.pkl")
