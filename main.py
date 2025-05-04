# main.py

from fetch_data import fetch_data
from train_model import train_model
from predict import predict_next, predict_next_rf
from evaluate import evaluate_prediction
from push_to_github import commit_and_push
from models.random_forest import save_model_rf
from visuals.visualization import plot_predictions
from visuals.visualization import plot_mae_evolution

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
    tickers = ["BTC/USDT", "ETH/USDT", "BNB/USDT"]
    results = []

    for ticker in tickers:
        try:
            data_dict = fetch_data(tickers=[ticker])
            data, _ = data_dict[ticker.replace("/", "")]
            model_type = decide_next_model()
            train_model(data, model_type=model_type)
            if model_type == "rf":
                save_model_rf()
            prediction = predict_next_rf(data) if model_type == "rf" else predict_next(data)

            y_true = get_real_close_price(data)
            mae = evaluate_prediction(y_true, prediction)
            from visualization import plot_predictions
            plot_predictions(y_true, prediction, model_name=model_type)

            results.append({
                "Ticker": ticker,
                "Model": model_type,
                "Prediction": round(prediction, 2),
                "Real": round(y_true, 2),
                "MAE": round(mae, 2)
            })

        except Exception as e:
            print(f"[ERROR] Ticker {ticker} failed with error: {type(e).__name__} - {e}")

    df_results = pd.DataFrame(results)
    print("\n[SUMMARY]")
    print(df_results)

    if results:
        mae_dict = {row["Ticker"]: row["MAE"] for row in results}
        plot_mae_evolution(mae_dict)

    commit_and_push()

if __name__ == "__main__":
    main()