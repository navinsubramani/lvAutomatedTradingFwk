# Get Interested Market Data

# Import required finance APIs, post processing APIs

import yfinance as yf
import numpy as np

def getTickerCurrentValue(Ticker):
    return 10

def getTickerHistoricData(Ticker, period, interval):
    # result = yf.download(tickers = Ticker, period = period, interval = interval)

    # Get the historic data values
    tik = yf.ticker.Ticker(Ticker)
    result = yf.ticker.Ticker.history(tik, period=period, interval= interval)
    print(result)

    # Get X index of the result as strings = Time Stamp & Open values as list
    ts = (result.index.values).astype(str)
    # print(ts)
    return ts.tolist(), result.values.tolist()

print(getTickerHistoricData("MSFT", "5d", "60m"))