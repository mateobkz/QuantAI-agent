# fetch_data.py

import ccxt
import pandas as pd
from datetime import datetime, timedelta

def fetch_data(ticker="BTC/USDT"):
    """
    Récupère 1 an de données OHLCV quotidiennes pour le ticker donné depuis Binance.
    """
    exchange = ccxt.binance()
    # Date de fin = aujourd'hui (UTC)
    end = datetime.utcnow()
    # Date de début = 1 an avant
    since = exchange.parse8601((end - timedelta(days=365)).strftime('%Y-%m-%dT00:00:00Z'))
    # Récupération des données
    ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1d', since=since, limit=365)
    # Construction du DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('Date', inplace=True)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    # Enregistrement du CSV
    today = datetime.utcnow().strftime('%Y-%m-%d')
    safe_ticker = ticker.replace('/', '')
    data_path = f"data/raw/{safe_ticker}_{today}.csv"
    df.to_csv(data_path)
    return df, data_path