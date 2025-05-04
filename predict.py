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
    """
    Charge le modèle Random Forest sauvegardé et génère une prédiction.
    """
    import joblib

    # Préparer les features
    X = data[["Open", "High", "Low", "Volume"]].iloc[[-1]]

    # Charger le modèle avec joblib
    model = joblib.load("models/random_forest_model.pkl")

    # Générer la prédiction
    prediction = model.predict(X)[0]
    return prediction