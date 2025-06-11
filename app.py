import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="📈 FlexBoard", layout="wide")
st.title("🚀 FlexBoard – Real-Time Stock Dashboard")

ticker = st.text_input("Enter a stock symbol (e.g. AAPL, TSLA, META)", value="AAPL")

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1mo")

        st.subheader(f"{info['longName']} ({ticker.upper()})")
        col1, col2, col3 = st.columns(3)

        col1.metric("📊 Price", f"${info['currentPrice']}")
        col2.metric("📈 52W High", f"${info['fiftyTwoWeekHigh']}")
        col3.metric("📉 52W Low", f"${info['fiftyTwoWeekLow']}")

        st.markdown("### 💹 Stock Price (Last Month)")
        st.line_chart(hist['Close'])

    except Exception as e:
        st.error("⚠️ Invalid stock symbol or error loading data.")
