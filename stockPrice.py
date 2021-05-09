# Importing the libraries

import yfinance as yf
import streamlit as st 
import pandas as pd 

# Writing the web app presentation

st.write("""
# Simple Stock Price App
# 
# Show are the stock closing price and volume of Google!
# 
# """)

# Define the ticker symbol (you could modify every time you want)
tickerSymbol = 'GOOGL'

# Get data on this ticker