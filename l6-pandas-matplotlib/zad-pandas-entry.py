import pandas as pd
# tasks from file 'pandas wprowadzenie.pdf'

tn = 3  # 1 or 3
match tn:
    case 1:
        df = pd.read_excel('datasets/imiona.xlsx')
        print(df)
# task #2
        print(df[df.Liczba > 1000])

        print(df[df.Imie == 'PAWEŁ'])

        print(df.Liczba.sum())

        print(df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']}))

        print(df.groupby('Plec').agg({'Liczba': ['sum']}))

        print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
# last subtask for #2
        df_ys = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
        # for index, group in enumerate(df_ys, start=1):
        #     print(f'{index}{group[0]}')
        #     print(f' {group[1].iloc[0]['Imie']}', end='')
        #     print(f' {group[1].iloc[0]['Liczba']}')
        group = df.groupby(['Rok', 'Plec']).agg('Liczba').max()
        # print(group)
        # for i, g in enumerate(group, start=1):
        #     print(i)
        #     print(df[df['Liczba'] == g])
        # group = df.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']})
        # print(group[max])
        # for i, g in enumerate(group[max], start=1):
        #     print(df[df['Liczba'] == g])
        print('Boy')
        print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']})
              .sort_values(('Liczba', 'sum'), ascending=False).iloc[0])
        print('Girl')
        print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']})
              .sort_values(('Liczba', 'sum'), ascending=False).iloc[0])
    case 3:
        df = pd.read_csv('datasets/zamowienia.csv',
                         header=0, sep=';', decimal='.')

        print(df['Sprzedawca'].unique())

        print(df.sort_values('Utarg', ascending=False).head(5))

        print(df.groupby('Sprzedawca').size())

        print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
        print(df.groupby('Kraj').size())

        print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01')
                 & (df['Data zamowienia'] <= '2005-12-31')].agg({'Utarg': ['sum']}))

        print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
        rok_2004 = df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
        rok_2004.to_csv("zamowienia_2004.csv", index=False)

