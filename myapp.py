import yfinance as yf
import streamlit as st


st.write("""
## Приложение цены обычной акции

Ниже показаны цена закрытия и объем торгов акции Эпл!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2024-1-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""*Цена закрытия*""")
st.line_chart(tickerDf.Close)
st.write("""Объем торгов""")
st.line_chart(tickerDf.Volume)

st.write("""Дивиденды компании""")
st.line_chart(tickerData.dividends)
st.write("""**Финансовые показатели**""")
tickerData.financials


