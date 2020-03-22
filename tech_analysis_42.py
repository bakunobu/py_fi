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
        DataFrame for meanipulation
    rolling_col: str
        column the prediction is based on (no check added)
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
sp500_pred = rolling_window(sp500_42d, 'Close', '252d', 252)

#print(sp500_pred[['Close', '42d', '252d']].tail(10))
#sp500_pred[['Close', '42d', '252d']].plot(grid=True, figsize=(8, 5))

#plt.show()

sp500_pred['42-252'] = sp500_pred['42d'] - sp500_pred['252d']
#print(sp500_pred['42-252'].tail())

#Regime func
SD = 50
sp500_pred['Regime'] = np.where(sp500_pred['42-252'] > SD, 1, 0)
sp500_pred['Regime'] = np.where(sp500_pred['42-252'] < -SD, - 1, sp500_pred['Regime'])
#print(sp500_pred['Regime'].value_counts())

#sp500_pred['Regime'].plot(lw=1.5)
#plt.ylim([-1.1, 1.1])
#plt.show()

sp500_pred['Market'] = np.log(sp500_pred['Close'] / sp500_pred['Close'].shift(1))
sp500_pred['Strategy'] = sp500_pred['Regime'].shift(1) * sp500_pred['Market']

sp500_pred[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True, figsize=(8,5))
plt.show()