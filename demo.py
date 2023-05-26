import pandas as pd
import yfinance as yf
from talib import MA

def get_stock_data(ticker_symbol, period='5m', start_date='2020-01-01', end_date='2022-12-31'):
    ticker_data = yf.Ticker(ticker_symbol)
    data = ticker_data.history(period=period, start=start_date, end=end_date)
    return data

def calculate_moving_average(data, period=77):
    return MA(data['Close'], timeperiod=period)

def find_buy_points(data, moving_average):
    buy_points = []

    for i in range(2, len(data)):
        # Find a point where the price was going up, then retraced but did not go lower than previous low, then goes up again
        if data['Low'][i-2] < data['Low'][i-1] and data['Low'][i] > data['Low'][i-1] and data['Close'][i] > data['Close'][i-1]:
            # Check if the moving average is flat or going up
            if moving_average[i-1] <= moving_average[i]:
                buy_points.append(i)

    return buy_points

# Replace 'AAPL' with your target stock symbol
data = get_stock_data('AAPL')
moving_average = calculate_moving_average(data)

buy_points = find_buy_points(data, moving_average)

print('Buy points:')
for i in buy_points:
    print(data.index[i])
