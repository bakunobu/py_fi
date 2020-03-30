import numpy as np
import pandas as pd
import sqlite3 as sq3

data = np.random.standard_normal((1_000_000, 5)).round(5)
filename = 'numbs'

query = 'CREATE TABLE numbers (No1 real, No2 real,\
    No3 real, No4 real, No5 real)'

con = sq3.Connection(filename+'.db')
con.execute(query)

con.executemany('INSERT INTO numbers VALUES (?, ?, ?, ?, ?)', data)
con.commit()