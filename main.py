# main.py

from fetch_data import fetch_data
from train_model import train_model
from predict import predict_next
from evaluate import evaluate_prediction
from push_to_github import commit_and_push

import pandas as pd
import json
import os

def get_current_model_type():
    try:
        with open("models/model_config.json", "r") as f:
            return json.load(f)["model_type"]
    except:
        return "linear"

def decide_next_model():
    perf_file = "data/performance.csv"
    if not os.path.exists(perf_file):
        return "linear"
    
    df = pd.read_csv(perf_file).tail(3)  # dernière 3 erreurs
    if df.shape[0] < 3:
        return "linear"
    
    mean_mae = df["mae"].mean()
    if mean_mae > 5:  # seuil à ajuster
        return "rf"
    return "linear"

def get_real_close_price(data):
    return data["Close"].iloc[-1]

def main():
    data, _ = fetch_data()
    model_type = decide_next_model()
    train_model(data, model_type=model_type)
    prediction = predict_next(data)

    y_true = get_real_close_price(data)
    mae = evaluate_prediction(y_true, prediction)

    print(f"[INFO] Model: {model_type} | Prediction: {prediction:.2f} | Real: {y_true:.2f} | MAE: {mae:.2f}")

    commit_and_push()

if __name__ == "__main__":
    main()