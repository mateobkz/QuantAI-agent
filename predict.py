# predict.py

import pickle
import pandas as pd

def predict_next(data):
    X = data[["Open", "High", "Low", "Volume"]].iloc[[-1]]

    # Load model
    with open("models/latest_model.pkl", "rb") as f:
        model = pickle.load(f)

    prediction = model.predict(X)[0]
    return prediction


# New function: predict_next_rf
def predict_next_rf(data):
    from sklearn.ensemble import RandomForestRegressor
    import joblib

    X = data[["Open", "High", "Low", "Volume"]].iloc[[-1]]

    # Load Random Forest model
    with open("models/random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)

    prediction = model.predict(X)[0]
    return prediction