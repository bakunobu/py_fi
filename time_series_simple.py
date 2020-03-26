import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

df2 = df.apply(lambda x: x ** 2)

df['floats'] = (1.5, 2.5, 3.5, 4.5)

df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'],
                           index=['d', 'a', 'b', 'c'])

df = df.append(pd.DataFrame({'numbers': 100,
                             'floats': 5.75,
                             'names': 'Henry'},
                            index=['z',]))
df3 = df.join(pd.DataFrame([1, 4, 9, 16, 25],
                     index=['a', 'b', 'c', 'd', 'y'],
                     columns=['squares',]),
              how='outer')



a = np.random.standard_normal((9, 4))
a.round(6)
dfa = pd.DataFrame(a)
dfa.columns = [['No1', 'No2', 'No3', 'No4']]


dates = pd.date_range('2015-1-1', periods=9, freq='M')
dfa.index = dates


#basic analytics

#print(dfa.sum())
#print(dfa.mean())
#print(dfa.cumsum())
#print(dfa.describe())
#print(np.sqrt(dfa))
#print(np.sqrt(dfa).sum())
#dfa.cumsum().plot(lw=2.0)



#Series class
dfa[['No1']].cumsum().plot(style='r', lw=2.0) #use an extra [ ] to send th column name as a list!
plt.xlabel('date')
plt.ylabel('value')
#plt.show()

#GroupBy operations
dfa['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
dfa.rename(columns = {'No1': 'N1',
                      'No2': 'N2',
                      'No3': 'N3',
                      'No4': 'N4',
                      'Quarter': 'Q'},
           inplace=True)

print(dfa.head())
cols_to_show = ['No1', 'No2', 'No3', 'No4']
print(dfa.groupby(['Q'], axis=1)[cols_to_show].mean())