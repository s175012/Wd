# import numpy as np
#
# a = np.array([1, 2, 3])  # string row
# print("a:", a)
# print("typ a:", type(a))
# b = np.array([1, 2, 3.0])  # float64 row
# print("b:", b)
# print("typ b:", type(b[1]))
# c = np.array([[1, 2], [3, 4]])
# print("c:", c)
# d = np.array([1, 2, 3], ndmin=2)  # min size 2
# print("d:", d)
# e = np.array([1, 2, 3], dtype=complex)
# print("e:", e)
# f = np.array(np.mat('1 2; 3 4'))  # still ndarray
# print("f:", f)
# print("typ f:", type(f))
# g = np.array(np.mat('1 2; 3 4'), subok=True)  # class is numpy.matrix
# print("g:", g)
# print(type(g))

# import numpy as np
# import time
#
# start_time = time.time()
# my_arr = np.arange(1000000)  # works 20?! times faster
# my_list = list(range(1000000))
# start_time = time.time()
# my_arr2 = my_arr * 2
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# my_list2 = [x * 2 for x in my_list]
# print("--- %s seconds ---" % (time.time() - start_time))

import numpy as np

tab1 = np.array([2, -3, 4, -8, 1])
print("typ:", type(tab1))
print("shape:", tab1.shape)
print("size:", tab1.size)  # number of data fields
print("ndim:", tab1.ndim)  # number of dimensions
print("nbytes:", tab1.nbytes)  # occupied space in mem
print("dtype:", tab1.dtype)  # data type
