import numpy as np

from random import gauss
import datetime

"""
Pickle
======
"""
import pickle

a = [gauss(1.5, 2) for i in range(1_000_000)]

delta = datetime.datetime.now()

pkl_file = open('data.pkl', 'wb') # 'w' key raises TypeError
pickle.dump(a, pkl_file)

print(datetime.datetime.now() - delta)
pkl_file.close()

pkl_file = open('data.pkl', 'rb') # 'r' key raises UnicodeDecodeError
b = pickle.load(pkl_file)
pkl_file.close()
print(b[:5])

delta = datetime.datetime.now()
pkl_file = open('data.pkl', 'wb')
pickle.dump(np.array(a), pkl_file)
pickle.dump(np.array(a) ** 2, pkl_file)
pkl_file.close()
print(datetime.datetime.now() - delta)


delta = datetime.datetime.now()
pkl_file = open('data.pkl', 'rb')
x = pickle.load(pkl_file)
y = pickle.load(pkl_file)

pkl_file = open('data.pkl', 'wb')
pickle.dump({'x': x, 'y': y}, pkl_file)
pkl_file.close()

pkl_file = open('data.pkl', 'rb')
data = pickle.load(pkl_file)
pkl_file.close()
for key in data.keys():
    print(key, data[key][:4])
    
print(datetime.datetime.now() - delta)

"""
CSV
===
"""
import pandas as pd
rows = 5000
a = np.random.standard_normal((rows, 5))
a = a.round(4)

t = pd.date_range(start='2014/1/1', periods=rows, freq='H')

with open('data.csv', 'w') as csv_file:
    header='date,no1,no2,no3,no4,no5\n'
    csv_file.write(header)
    for t_, (no1,no2,no3,no4,no5) in zip(t, a):
        s = '%s,%f,%f,%f,%f,%f\n' % (t_, no1, no2, no3, no4, no5)
        csv_file.write(s)
        

with open('data.csv', 'r') as csv_file:
    content = csv_file.readlines()
    for line in content[:5]:
        print(line,)




