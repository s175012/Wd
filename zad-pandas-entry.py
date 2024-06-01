import pandas as pd
import numpy as np

tn = 1  # 1 or 3
match tn:
    case 1:
        df = pd.read_excel('datasets/imiona.xlsx')
        print(df)
        stn = 1
        match stn:
            case 1:
                names_by_year = df.groupby('Rok').agg({'Imie': ['count']}) > 1000
                print(names_by_year.iloc[])
                        # print('')
