import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
# df = pd.read_csv('dane.csv', header=0, sep=';')  # after ending of pandas on teams
# print(df)
df.to_csv('plik.csv', index=False)

# print(s['c'])
# print(s.c)
# print(df[0:1])
# print('')
# print(df['Populacja'])
# print(df.iloc[0, 0])
# print(df.loc[0, 'Kraj'])
# print(df.at[0, 'Kraj'])
# print('kraj: ' + df.Kraj)
# print(df.sample())
#
# print(df.sample(2))
# print(df.sample(frac=0.5))
# print(df.sample(n=10, replace=True))
# print(df.head())
# print(df.head(2))
# print(df.tail(1))
# print(df.describe())
# print(df.T)

# print(s[(s > 9)])
# print(s.where(s > 10))
# print(s.where(s > 10, 'za duże'))
# seria = s.copy()
# seria.where(seria > 10, 'za duże', inplace=True)
# print('########')
# print(seria)

# print(s[~(s > 10)])
#
# print(s[(s < 13) & (s > 8)])

# print(df[(df.Populacja > 10**6) & df.index.isin([0, 2])])
#
# print('########')
# szukaj = ['Belgia',  'Brasilia']
# print(df.isin(szukaj))

# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)
#
df.loc[3] = 'dodane'
print(df)
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)

new_df = df.drop([3])
print(new_df)

df.drop([3], inplace=True)
print(df)

# df.drop('Kraj', axis=1, inplace=True)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

# 1.06.24 continued

print(df.sort_values(by='Kraj'))
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))
print(df.groupby(['Kontynent']).agg('Populacja').sum())
