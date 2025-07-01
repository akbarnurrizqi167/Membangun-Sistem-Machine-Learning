import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Aktifkan autolog MLflow
mlflow.sklearn.autolog()

# Baca data hasil preprocessing
train_df = pd.read_csv("dataset_preprocessing/train.csv")

# Pisahkan fitur dan target
X_train = train_df.drop(columns=["Churn"])
y_train = train_df["Churn"]

# Untuk validasi internal (optional), bisa gunakan sebagian dari train_df
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, stratify=y_train, random_state=42)

# Buat model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Jalankan experiment MLflow
with mlflow.start_run():
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {acc:.4f}")
