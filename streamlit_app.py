import streamlit as st
import pandas as pd
import requests
import time
from datetime import datetime

# 🔑 Your Polygon.io API Key
API_KEY = "FNQ6kulx77olUBTnhrTfbaklew20b3vt"

# Magnificent 7 + SPY
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "SPY"]

# Fetch last trade data from Polygon
def get_trade(symbol):
    url = f"https://api.polygon.io/v2/last/trade/{symbol}?apiKey={API_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()["results"]
        return {
            "Sym": symbol,
            "Price": data.get("p"),
            "Size": data.get("s"),
            "Exchange": data.get("x"),
            "Timestamp": datetime.fromtimestamp(data.get("t") / 1e9).strftime("%H:%M:%S.%f")[:-3]
        }
    else:
        return {
            "Sym": symbol,
            "Price": "N/A",
            "Size": "N/A",
            "Exchange": "N/A",
            "Timestamp": "Error"
        }

st.title("📡 Live Time & Sales: Magnificent 7 + SPY (Delayed)")

placeholder = st.empty()

while True:
    rows = [get_trade(sym) for sym in symbols]
    df = pd.DataFrame(rows)
    with placeholder.container():
        st.dataframe(df)
    time.sleep(5)  # update every 5 seconds

