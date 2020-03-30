import numpy as np
import tables as tb
import datetime as dt
import matplotlib.pyplot as plt


filename = 'tab.h5'
h5 = tb.open_file(filename, 'w')

rows = 2_000_000
row_des = {
    'Date': tb.StringCol(26, pos=1),
    'No1': tb.IntCol(pos=2),
    'No2': tb.IntCol(pos=3),
    'No3': tb.Float64Col(pos=4),
    'No4': tb.Float64Col(pos=5)
}

filters = tb.Filters(complevel=0)
tab = h5.create_table('/', 'ints_floats', row_des,
                      title='Integers and Floats',
                      expectedrows=rows, filters=filters)

pointer = tab.row

ran_int = np.random.randint(0, 10000, size=(rows, 2))
ran_flo = np.random.standard_normal((rows, 2)).round(5)

start = dt.datetime.now()

for i in range(rows):
    pointer["Date"] = dt.datetime.now()
    pointer['No1'] = ran_int[i, 0]
    pointer['No2'] = ran_int[i, 1]
    pointer['No3'] = ran_flo[i, 0]
    pointer['No4'] = ran_flo[i, 1]
    pointer.append()

tab.flush()
plt.hist(tab[:]['No3'], bins=30)
plt.grid(True)
#plt.show()

res = np.array([(row['No3'], row['No4']) for row in
                tab.where('((No3 < -0.5) | (No3 > 0.5)) \
                    & ((No4 < -1) | (No4 > 1))')])[::100]
plt.plot(res.T[0], res.T[1], 'ro')
plt.grid(True)

#plt.show()

values = tab.cols.No3[:]

print('Max %18.3f' % values.max())
print('Aver %18.3f' % values.mean())
print('Min %18.3f' % values.min())
print('Std %18.3f' % values.std())



results = [(row['No1'], row['No2']) for row in
           tab.where('((No1 > 9800) | (No2 < 200)) \
               & ((No2 > 4500) & (No2 < 5500))')]

for res in results[:4]:
    print(res)
    
results = [(row['No1'], row['No2']) for row in
           tab.where('(No1 == 1234) & (No2 > 9776)')]

for res in results:
    print(res)

print(dt.datetime.now() - start)