import yfinance as yf
import pandas as pd
import os

tickers = ["XOM", "CVX", "XLE", "XOP", "NEM", "GOLD", "ADM", "BG"]

# download adjusted OHLCV data
data = yf.download(tickers, start="2015-01-01", auto_adjust=True)

# create a data folder
os.makedirs("data", exist_ok=True)

# save each field separately (Close, Volume, etc.) as CSV
for field in ["Close", "Volume", "Open", "High", "Low"]:
    data[field].to_csv(f"data/raw/{field.lower()}.csv")

print("Saved to data/")