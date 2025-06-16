import ccxt
import pandas as pd
import ta
import streamlit as st
import matplotlib.pyplot as plt
import datetime

# === Configuration ===
symbol = 'BTC/USDT'
timeframe = '1h'
rsi_period = 14
rsi_oversold = 30
rsi_overbought = 70

# === Streamlit Page Setup ===
st.set_page_config(page_title="BTC 1H RSI Scalping Bot", layout="wide")
st.title("📈 BTC/USDT 1H RSI Scalping Bot Visualizer")

# === Connect to Binance ===
exchange = ccxt.binance({'enableRateLimit': True})

@st.cache_data(ttl=3600)
def fetch_ohlcv():
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('datetime', inplace=True)
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=rsi_period).rsi()
    return df

df = fetch_ohlcv()

# === Generate Signal ===
last_rsi = df['rsi'].dropna().iloc[-1]
if last_rsi < rsi_oversold:
    signal = '🟢 BUY'
elif last_rsi > rsi_overbought:
    signal = '🔴 SELL'
else:
    signal = '⚪ HOLD'

# === Show RSI Plot ===
fig, ax = plt.subplots(figsize=(10, 4))
df['rsi'].plot(ax=ax, label='RSI', color='blue')
ax.axhline(rsi_oversold, color='green', linestyle='--', label='Oversold (30)')
ax.axhline(rsi_overbought, color='red', linestyle='--', label='Overbought (70)')
ax.set_title(f"RSI (Last: {last_rsi:.2f}) | Signal: {signal}")
ax.set_ylabel("RSI Value")
ax.legend()
st.pyplot(fig)

# === Show Table ===
with st.expander("Show Raw Data"):
    st.dataframe(df[['close', 'rsi']].tail(20))
