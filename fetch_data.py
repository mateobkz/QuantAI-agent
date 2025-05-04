# fetch_data.py

import ccxt
import pandas as pd
from datetime import datetime, timedelta

def fetch_data(tickers=["BTC/USDT"]):
    """
    Récupère 1 an de données OHLCV quotidiennes pour les tickers donnés depuis Binance.
    """
    exchange = ccxt.binance()
    end = datetime.utcnow()
    since = exchange.parse8601((end - timedelta(days=365)).strftime('%Y-%m-%dT00:00:00Z'))
    
    results = {}

    for ticker in tickers:
        try:
            ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1d', since=since, limit=365)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
            df['Date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('Date', inplace=True)
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
            today = datetime.utcnow().strftime('%Y-%m-%d')
            safe_ticker = ticker.replace('/', '')
            data_path = f"data/raw/{safe_ticker}_{today}.csv"
            df.to_csv(data_path)
            if df.empty:
                print(f"[WARNING] No valid data fetched for {ticker}.")
            results[safe_ticker] = (df, data_path)
        except Exception as e:
            print(f"[ERROR] Failed to fetch data for {ticker}: {e}")
            results[ticker.replace('/', '')] = (None, None)

    return results