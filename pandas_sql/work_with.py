import numpy as np
import pandas as pd
import sqlite3 as sq3
import matplotlib.pyplot as plt
# pip3 install tables
# pip3 install openpyxl
# pip3 install xlrd

con = sq3.Connection('numbs.db')

temp = con.execute('SELECT * FROM numbers').fetchall()
#print(temp[:2])

query = 'SELECT * FROM numbers WHERE No1 > 0 AND No2 < 0'
res = np.array(con.execute(query).fetchall()).round(3)
"""
plt.plot(res[:, 0], res[:, 1], 'ro')
plt.grid(True)
plt.xlim(-0.5, 4.5)
plt.ylim(-4.5, 0.5)
plt.show()

"""

data = pd.read_sql('SELECT * FROM numbers', con)
#print(data[(data['No1'] > 0) & (data['No2'] < 0)].head())

res = data[['No1', 'No2']][((data['No1'] > 0.5) | (data['No1'] < -0.5))
                           & ((data['No2'] < -1) | (data['No2'] > 1))]

'''
plt.plot(res.No1, res.No2, 'ro')
plt.grid(True)
plt.axis('tight')
plt.show()
'''
"""
h5s = pd.HDFStore('numbs.h5s', 'w')
h5s['data'] = data
h5s.close()
"""
"""
data.to_csv('numbs.csv')
pd.read_csv('numbs.csv')[['No1', 'No2', 'No3', 'No4']].hist(bins=20)
"""

data[:100000].to_excel('numbs.xlsx')


#pd.read_excel('numbs.xlsx', 'Sheet1').cumsum().plot()
df = pd.read_excel('numbs.xlsx', 'Sheet1')
df = df[['No1', 'No2', 'No3', 'No4', 'No5']]
df.cumsum().plot()

plt.show()
