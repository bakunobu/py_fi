import numpy as np
import pandas as pd
import pandas.io.data as web

goog = web.DataReader('GOOG', data_source='google',
                      start='3/14/2009', end='4/14/2014')

print(goog.tail())
