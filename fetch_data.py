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
        # conserver le ticker d’origine pour le dictionnaire
        ticker_input = ticker
        try:
            # Tentative sur Binance
            try:
                ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1d', since=since, limit=365)
            except Exception as e:
                print(f"[WARNING] Binance failed for {ticker}: {e}, falling back to Kraken")
                # Fallback vers Kraken avec paire USD
                exchange = ccxt.kraken()
                alt_ticker = ticker.replace('/USDT', '/USD')
                ohlcv = exchange.fetch_ohlcv(alt_ticker, timeframe='1d', since=since, limit=365)
                ticker = alt_ticker

            # Construction du DataFrame
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
            df['Date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('Date', inplace=True)
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

            # Sauvegarde des données
            today = datetime.utcnow().strftime('%Y-%m-%d')
            safe_ticker = ticker.replace('/', '')
            data_path = f"data/raw/{safe_ticker}_{today}.csv"
            df.to_csv(data_path)
            if df.empty:
                print(f"[WARNING] No valid data fetched for {ticker}.")

            # Utilise la clé d’origine pour le résultat
            safe_key = ticker_input.replace('/', '')
            results[safe_key] = (df, data_path)
        except Exception as e:
            print(f"[ERROR] Failed to fetch data for {ticker_input}: {e}")
            safe_key = ticker_input.replace('/', '')
            results[safe_key] = (None, None)

    return results