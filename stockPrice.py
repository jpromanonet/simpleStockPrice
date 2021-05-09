# Importing the libraries

import yfinance as yf
import streamlit as st 
import pandas as pd 

# Writing the web app presentation

st.write("""
# Simple Stock Price App

Show are the stock closing price and volume of Google!

""")

# Define the ticker symbol (you could modify every time you want)
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker for the last decade
# Modify the period value if you want a bigger or smaller range
tickerDf = tickerData.history(period='1d', start='2011-5-9', end='2021-5-9')

# Open High Low Close Volume Dividends Stock Splits

# Now show the volume and close values with streamlit
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)