import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt



sp500 = web.DataReader('^GSPC', data_source='yahoo',
                       start='1/1/2000', end='4/14/2014')


#sp500['42d'] = np.round(sp500['Close'].rolling(42).mean(), 2)
#print(sp500.tail(10))


def rolling_window(df, rolling_col, new_col_name, window):
    '''
    
    A rolling window for a time series that uses pandas rolling func
    
    Vars
    ====
    df: Pandas DataFrame type object
        DataFrame with a specified col name (df['col_name'])
    rolling_col: str
        column the prediction is based on
    new_col_name: str
        a name of a new olumn with predicted data
    window: int
        a trend period
    args: not specified
        some additional params for the pandas rolling method
    
    Returns
    =======
    The modified Pandas DataFrame type object with a forecasting column added
    (all the values in the column are rounded (np.round(value, 3)))
    '''
    
    df[new_col_name] = np.round(df[rolling_col].rolling(window).mean(), 2)
    return(df)

sp500_42d = rolling_window(sp500, 'Close', '42d', 42)
print(sp500_42d['42d'].tail(10))