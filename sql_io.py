import sqlite3 as sq3
import numpy as np
import datetime


query = 'CREATE TABLE numbs (Date date, No1 real, No2 real)'
con =sq3.connect('numbs.db')

con.execute(query)
con.commit()

con.execute('INSERT INTO numbs VALUES(?, ?, ?)',
            (datetime.datetime.now(), 0.12, 7.3))

data = np.random.standard_normal((10000, 2)).round(5)
for row in data:
    con.execute('INSERT INTO numbs VALUES(?, ?, ?)',
                (datetime.datetime.now(), row[0], row[1]))

con.commit()