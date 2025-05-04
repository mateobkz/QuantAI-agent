from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np

def train_and_predict(X_train, y_train, X_test, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return predictions, mae, model

import joblib
import os

def save_model(model, filename="random_forest_model.pkl"):
    model_path = os.path.join("models", filename)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def save_model_rf(model):
    save_model(model, filename="random_forest_model.pkl")