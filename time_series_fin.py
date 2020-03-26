import math
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from tech_analysis_42 import rolling_window #see in dir

DAX_2000 = web.DataReader('^GDAXI', data_source='yahoo',
                       start='1/1/2000')

#print(DAX_2000.head()) #tested:OK


#DAX_2000['Close'].plot(figsize=(8, 5))
"""
DAX_2000['Ret_Loop'] = 0.0


for i in range(1, len(DAX_2000)):
    DAX_2000['Ret_Loop'][i] = np.log(DAX_2000['Close'][i] / DAX_2000['Close'][i-1])
del DAX_2000['Ret_Loop']
"""
DAX_2000['Return'] = np.log(DAX_2000['Close'] / DAX_2000['Close'].shift(1))

#print(DAX_2000[['Close', 'Return']].tail())
"""
DAX_2000[['Close', 'Return']].plot(subplots=True, style='b',
                                   figsize=(8, 5))
"""

DAX_2000 = rolling_window(DAX_2000, 'Close', '42d', 42)
DAX_2000 = rolling_window(DAX_2000, 'Close', '252d', 252)

# DAX_2000[['Close', '42d', '252d']].plot(figsize=(8,5))
DAX_2000['Mov_Vol'] = DAX_2000['Return'].rolling(252).std() * math.sqrt(252)


DAX_2000[['Close', 'Mov_Vol', 'Return']].plot(subplots=True,
                                              style='b',
                                              figsize=(8,5))
plt.show()
#print(DAX_2000.tail())