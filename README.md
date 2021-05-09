# simpleStockPrice

A simple stock price data science project made with Python and Streamlit

## Development Journal

1. Install streamlit using:

   ```
   pip3 install streamlit
   ```

2. If when trying to use the "streamlit hello" command you get an error, try this

   ```
   pip3 install protobuf --upgrade
   ```

   Then run "streamlit hello" again and it should work just fine.

3. Now we should install pandas and yfinance, which we are going to use in the python file.

   ```
   pip3 install pandas
   pip3 install yfinance
   ```

## How to run the Simple Stock Price app

```
streamlit run stockPrice.py
```

It will open a browser tab at:

```
http://localhost:8502
```

Remember! you can change the ticker handler in the "tickerSymbol" variable and the time range for Close prices and volume in the "period" paramenter for tickerDf function.
