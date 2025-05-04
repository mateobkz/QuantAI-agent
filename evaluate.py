# evaluate.py

import pandas as pd
import os
from datetime import datetime
from sklearn.metrics import mean_absolute_error

def evaluate_prediction(y_true, y_pred):
    mae = abs(y_true - y_pred)

    # Chargement ou création de performance.csv
    performance_file = "data/performance.csv"
    if os.path.exists(performance_file):
        df = pd.read_csv(performance_file)
    else:
        df = pd.DataFrame(columns=["date", "y_true", "y_pred", "mae"])

    today = datetime.today().strftime("%Y-%m-%d")
    new_row = {"date": today, "y_true": y_true, "y_pred": y_pred, "mae": mae}
    df = pd.concat([df, pd.DataFrame([new_row])])
    df.to_csv(performance_file, index=False)

    return mae