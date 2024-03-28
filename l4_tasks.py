import numpy as np

tn = 6

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
    case 4:
        def generate_powers(base, degree):
            return np.logspace(1, degree, num=degree, base=base)
        print(generate_powers(2, 10))
    case 5:
        def generate_diagonal_matrix(row_length):
            return np.diag(np.linspace(row_length, 1, num=row_length*2))
        print(generate_diagonal_matrix(3))
    case 6:
        word_search = np.matrix([['t', 'a', 'c', 'o'],
                                 ['a', 's', 'd', 'c'],
                                 ['o', 'h', 'u', 'o'],
                                 ['c', 't', 'a', 'n']], dtype=str)
        print(word_search)
    case 7:
        def gen_mul_2_diag_matrix(n):
            matrix = np.diag(2*np.ones(n))
            for i in range(1, n):
                matrix[i:n, 0:n-i] += np.diag((i+1)*2*np.ones(n-i))
                matrix[0:n-i, i:n] += np.diag((i+1)*2*np.ones(n-i))
            return matrix
        print(gen_mul_2_diag_matrix(3))
    case 8:
        def divide_array(array, direction):
            print(type(int(array.shape[0])))
            if direction == 'v':
                if array.shape[0] % 2:
                    return 0
                return array[0:int(array.shape[0])//2, :], array[int(array.shape[0])//2:, :]
            if direction == 'h':
                if array.shape[1] % 2:
                    return 0
                return array[:, 0:int(array.shape[0])//2], array[:, int(array.shape[0])//2:]
        m = np.array((range(2), range(2)), dtype='int8')
        print(divide_array(m, 'h'))
    case 9:
        Fibonacci_matrix = np.array(np.zeros(25), dtype=int)
        Fibonacci_matrix[1] = 1
        for i in range(2, 25):
            Fibonacci_matrix[i] = Fibonacci_matrix[i-1] + Fibonacci_matrix[i-2]
        print(Fibonacci_matrix.reshape((5, 5)))
