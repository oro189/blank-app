import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# Dummy symbols and auction prices
symbols = ["NVDA.NQ", "FXI.AM", "INTC.NQ", "BAC.NY", "TLT.NQ", "VALE.NY", "AVGO.NQ", "MCHP.NQ", "SLB.NY", "SPY.AM"]
sources = ["NSDQ", "ARCA", "NYSE", "BRKR"]
sides = ["B", "S"]

def generate_data():
    data = []
    for _ in range(10):
        sym = random.choice(symbols)
        side = random.choice(sides)
        size = f"{round(random.uniform(1.5, 6.5), 3)}M"
        pv = f"{round(random.uniform(1.0, 25.0), 2)}M"
        mkt_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        src = random.choice(sources)
        auc_price = round(random.uniform(2.0, 500.0), 2)
        data.append([sym, side, size, pv, mkt_time, src, auc_price])
    return pd.DataFrame(data, columns=["Sym", "Side", "Size", "PV", "MktTm", "Tp Src", "AucPx"])

st.title("📉 Time & Sales Viewer")

placeholder = st.empty()

while True:
    df = generate_data()
    with placeholder.container():
        st.table(df)
    time.sleep(1)
