import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Aktifkan autolog MLflow
mlflow.sklearn.autolog()

# Load dataset hasil preprocessing
df = pd.read_csv("dataset_preprocessing/train.csv")

# Pisahkan fitur dan target
X = df.drop(columns=["Churn"])
y = df["Churn"]

# Split ulang data
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Parameter grid untuk tuning
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
}

# Inisialisasi model
rf = RandomForestClassifier(random_state=42)

# Mulai tracking MLflow
with mlflow.start_run():
    # Grid Search
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        scoring="accuracy",
        cv=3,
        n_jobs=-1
    )
    grid_search.fit(X_train, y_train)

    # Ambil model terbaik
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_val)
    acc = accuracy_score(y_val, y_pred)

    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Validation Accuracy: {acc}")
