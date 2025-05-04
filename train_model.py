# train_model.py

import pandas as pd
import pickle
import json
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def train_model(data, model_type="linear"):
    X = data[["Open", "High", "Low", "Volume"]]
    y = data["Close"].shift(-1)
    data = data.dropna()

    X = X[:-1]
    y = y[:-1]

    if model_type == "linear":
        model = LinearRegression()
    elif model_type == "rf":
        model = RandomForestRegressor(n_estimators=100)
    else:
        raise ValueError("Unknown model type")

    model.fit(X, y)

    # Save model
    with open("models/latest_model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save model config
    config = {"model_type": model_type}
    with open("models/model_config.json", "w") as f:
        json.dump(config, f)

    return model