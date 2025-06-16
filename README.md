# 📈 BTC 1H RSI Scalping Bot (Streamlit App)

A simple Streamlit application that visualizes the RSI (Relative Strength Index) for BTC/USDT on the 1-hour timeframe and provides basic scalping signals (Buy, Sell, Hold) using CCXT and technical indicators.

---

## 🚀 Features

- Uses Binance API via CCXT to fetch 1-hour OHLCV data
- Calculates RSI using `ta` library
- Plots RSI chart with overbought (70) and oversold (30) levels
- Displays real-time trading signal: 🟢 Buy / 🔴 Sell / ⚪ Hold
- Optional raw data table with close prices and RSI values

---

## ⚙️ HOW TO RUN

### ▶️ Using Dockerfile

```bash
docker build -t btc-scalping-app .
docker run -p 8501:8501 btc-scalping-app
```

### ▶️ Directly From Files

```bash
pip install -r requirements.txt
streamlit run main.py

Then open your browser and go to:
http://localhost:8501
```

💬 License
MIT License 
---

Let me know if you want to:
- Include screenshots
- Add GIFs of the app
- Include automatic refresh or trade execution logs in the README



![overbought](https://github.com/user-attachments/assets/74dc04ab-2c27-4d6e-aea0-b2ecf83415be)

