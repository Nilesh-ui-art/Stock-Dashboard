import yfinance as yf

def get_realtime_stock_data(symbol):
    stock = yf.Ticker(symbol + '.NS')
    data = stock.history(period='1d')
    return data

def get_historical_stock_data(symbol, period):
    stock = yf.Ticker(symbol + '.NS')
    data = stock.history(period=period)
    return data

def get_dividends_data(symbol):
    stock = yf.Ticker(symbol + '.NS')
    dividends = stock.dividends
    return dividends