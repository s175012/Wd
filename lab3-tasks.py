from random import *
from math import *

t_num = 3

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
        l1 = list({x: y for x, y in dic1.items() if y == 'pcs'})
        print(l1)
    case 4:
        def is_tr_rect(a, b, c):
            print("Triangle", a, ',', b, ',', c)
            a **= 2
            b **= 2
            c **= 2
            if a + b == c or b + c == a or c + a == b:
                print('has 90 degree angle.')
                return 1
            else:
                print("doesn't have 90 degree angle.")
        is_tr_rect(1.5, 2, 2.5)
    case 5:
        def tr_ar(a=1.0, b=2.0, h=3.0):
            print('The area of the trapezium', a, ',', b, ',', h)
            h *= (a+b)/2
            print('equals', h)
        tr_ar()
        tr_ar(2.5, 6.4, 1.4)
    case 6:
        def mul_geo_se(a1=1.0, b=4.0, ile=10):
            print('Multiplication of geometric sequence', a1, ',', b, ',', ile)
            for i in range(1, ile):
                a1 *= b**i
            print('equals', a1)
        mul_geo_se()
        mul_geo_se(1, 2, 1)
        mul_geo_se(1, 2, 3)
    case 7:
        x = float(input('Type positive number: '))
        print('Real square root from', x)
        try:
            x = sqrt(x)
            print('equals', x)
        except ValueError:
            print('does not exist.')
