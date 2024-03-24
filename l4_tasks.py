import numpy as np

tn = 3

match tn:
    case 1:
        a = np.arange(6, 51, 3)
        print(a)
    case 2:
        a = np.array([2.3, -9.5], dtype=float)
        print(a)
        b = a.astype('int64')
        print(b)
    case 3:
        def c_a(n):
            m = np.array([range(1, n * n + 1)])
            return m.reshape(n, n)
        print(c_a(6))
