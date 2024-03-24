import numpy as np

# a = np.array([0, 1])  # dim = 1 wektory, more matrices
# print(a)
#
# a = np.arange(2)
# print(a)
# print(type(a))
#
# print(a.dtype)
#
# a = np.arange(2, dtype='int32')
# print(a.dtype)
# b = a.astype('float')  # same
# print(b)
# print(b.dtype)
# print(b.shape)
#
# print(a.ndim)

# m = np.array((np.arange(2), np.arange(2)))
# print(m)
# print(m.shape)
# print(m.shape)
# print(m.ndim)
#
# matrix = np.array([[1, 2], [3, 4], [5, 6]])  # all rows need to be same length or error
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# zeros = np.zeros((5, 5))
# ones = np.ones((4, 4))
# print(zeros)
# print(ones)
# print(zeros.dtype)
# print(ones.dtype)
#
# empty = np.empty((2, 2))  # random stuff in, can change between runs
# print(empty)
# place_1 = empty[1, 1]
# print(place_1)
# place_2 = empty[0, 1]
# print(place_2)

# matrix = np.array([[1, 2], [3, 4]])
# print(matrix)
# numbers = np.arange(1, 2, 0.1)
# print(numbers)
#
# linear_numbers = np.linspace(1, 2, 5)  # linear space from closed interval
# print(linear_numbers)  # endpoint=false
#
# z = np.indices((5, 3))  # 2 matrices 5x3
# print(z)
# print(z[0])  # get 1. of them. 3 indexes required for a field
# print(z[0, 1, 2])  # then row, then column
#
# x, y = np.mgrid[0:5, 0:5]  # as above but to different variables and 5x5
# print(x)
# print(y)
#
# mat_diag = np.diag([a for a in range(5)], k=1)
# print(mat_diag)
#
# z = np.fromiter(range(5), dtype='int32')  # vector
# print(z)

# chars = b'abcdef'
# ch1 = np.frombuffer(chars, dtype='S1')  # int dividers of 6
# ch2 = np.frombuffer(chars, dtype='S2')
# print(ch1)
# print(ch2)

# chs = 'abcdef'
# ch3 = np.array(list(chs))
# ch4 = np.array(list(chs), dtype='S1')
# ch5 = np.array(list(b'abcdef'))  # ascii
# ch6 = np.fromiter(chs, dtype='S1')
# ch7 = np.fromiter(chs, dtype='U1')  # unicode type
# print(ch3)
# print(ch4)
# print(ch5)
# print(ch6)
# print(ch7)

# m = np.ones((2, 2))
# m1 = np.ones((2, 2))
# m += m1
# print(m)
# print(m - m1)
# m1 = np.array([[3, 4], [5, 6]])
# print(m*m1)  # element by element
# print(m/m1)  # as above
#
# a = np.dot(m, m1)  # multiply matrices by linear algebra
# print(a)
# b = m.dot(m1)
# print(b)

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])

# m = np.arange(25)
#
# m = m.reshape(5, 5)
# print(m)
#
# print(m[1:])  # all rows after 1.
# print(m[:, 1])  # last row
# print(m[:-1])  # all rs before last
# print(m[2:6, 1:3])  # 2. to 4. rs, 1. to 2. cs
# print(m[:, range(2, 6, 2)])
# print('')

x = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]  # ended with corner vals from x
print(y)
