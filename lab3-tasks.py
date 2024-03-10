from random import *
from math import *

t_num = 4

match t_num:
    case 1:
        A = [1-x for x in range(1, 11)]
        print(A)
        B = [4 ** x for x in range(8)]
        print(B)
        C = [x for x in B if x % 2 == 0]
        print(C)
    case 2:
        lis1 = []
        for i in range(10):
            lis1.append(floor(random()*10.0))
        print(lis1)
        lis_2div = [x for x in lis1 if x % 2 == 0]
        print(lis_2div)
    case 3:
        dic1 = {'pasta': 'pcs', 'tomato': 'kgs', 'cheese': 'kgs', 'sauce': 'pcs'}
        print(dic1)
        # l1 = [x for x in dic1.keys() if dic1.values() == 'pcs']
        # print(l1)  # how?
    # case 4:
        # def is_tr_rect  # to do
