"""
As far as finance module has been dropped from matplotlib releases 
we have to use another instruments

Some of them are quite similar to the old ones, but other aren't.

For example, you can't access historical data via . quotes_historical_yahoo method
and have to use another library (or do it by yourself). I prefer Pandas Datareader.
"""

import mplfinance as mpf #!pip3 install --upgrade mplfinance
from mpl_finance import candlestick_ohlc, plot_day_summary_oclh #!pip3 install mpl_finance
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas.util.testing import assert_frame_equal
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


'''
quotes = mpf.quotes_historical_yahoo('^GDAXI', start, end) # doesn't work
'''
quotes = web.DataReader('^GDAXI', data_source='yahoo', #don't use 'google' as a data_source
                      start='5/1/2014', end='6/30/2014')

kwargs = dict(type='candle', volume=True,figratio=(10,8),figscale=0.75, y_on_right=False)
mpf.plot(quotes, **kwargs, style='yahoo') #simple one-liner using mplfinance

"""
#Doing it hard way using old version of mpl_finance
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
candlestick_ohlc(ax, zip(mdates.date2num(quotes.index.to_pydatetime()),
                         quotes['Open'], quotes['High'],
                         quotes['Low'], quotes['Close']),
                         width=0.6, colorup='b', colordown='r')
plt.grid = True
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
"""
#mpf.plot(quotes, type='ohlc', style='charles') #easy way but colour blind

"""
#doing hard way
fig, ax = plt.subplots(figsize=(8, 5))
plot_day_summary_oclh(ax, zip(mdates.date2num(quotes.index.to_pydatetime()),
                         quotes['Open'], quotes['High'],
                         quotes['Low'], quotes['Close']),
                      colorup='b', colordown='r')
ax.autoscale_view()
#ax.xaxis.grid(True, 'major')
plt.grid(True)
ax.xaxis_date()

fig.autofmt_xdate()

plt.show()
"""