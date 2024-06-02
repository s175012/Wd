# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     # print(result)
# # except ZeroDivisionError:
# #     print("Error")
# # except ValueError:
# #     print('wrong value')
# except Exception:
#     print('error')
# else:
#     print(result)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l2 = [i**2 for i in l1]
# print(l2)
# l3 = [3**y for y in range(1, 6)]
# print(l3)
# l4 = [x for x in l1 if x % 2 == 1]
# print(l4)
# l5 = [(x, y) for x in l2 for y in l3]
# print(l5)
#
# l6 = []
# for i in l2:
#     for j in l3:
#         l6.append((i, j))
# print(l6)

# s1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}
# s2 = {}
# for key, value in s1.items():
#     s2[key] = value
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)

from math import *  # and we no longer write math. for mlib functions


# def quadra_equation(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('No real roots')
#         return 0
#     elif delta == 0:
#         print('one real root')
#         x = (-b / 2 * a)
#         return x
#     elif delta > 0:
#         print('two real roots')
#         x1 = (-b + sqrt(delta)) / (2 * a)
#         x2 = (-b - sqrt(delta)) / (2 * a)
#         return x1, x2
#
#
# print(quadra_equation(6, 3, 1))
# print(quadra_equation(1, 2, 1))
# print(quadra_equation(2, 6, 1))

# def part_len(x1=1, x2=2, y1=3, y2=4):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
#
#
# print(part_len())  # with defaults
# print(part_len(3, 5, 1, 6))  # preserved orig. order
# print(part_len(y1=5, x1=3, y2=6, x2=8))  # needed to specify cause different order
# print(part_len(1, 5, y2=8, y1=3))

# fil = open('tekst.txt', 'r', encoding='utf-8')
# cha = fil.read(10)
# line = fil.readline()
# lines = fil.readlines()
# fil.close()
# print(cha)
# print(line)
# print(lines)
# fil = open('tekst.txt', 'a+')  # adds on file end, + can also read
# fil.write('aaaaa')
# fil.seek(105)  # go to index 105 in file
# cha = fil.read(10)
# fil.close()
# print(cha)

with open('../tekst.txt', 'r') as fil:  # closes automatically
    cha = fil.read(10)

print(cha)
