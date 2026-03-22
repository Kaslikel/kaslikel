# Simple Moving Average Strategy Example

import pandas as pd

def moving_average_strategy(data, short_window=5, long_window=20):
    data['SMA_short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window).mean()

    data['Signal'] = 0
    data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = 1
    data.loc[data['SMA_short'] < data['SMA_long'], 'Signal'] = -1

    return data

print("Basic trading strategy loaded.")
