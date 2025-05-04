# fetch_data.py

import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_data(ticker="AAPL", period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    data = data[["Open", "High", "Low", "Close", "Volume"]]
    data.dropna(inplace=True)

    today = datetime.today().strftime('%Y-%m-%d')
    data_path = f"data/raw/{ticker}_{today}.csv"
    data.to_csv(data_path)
    return data, data_path