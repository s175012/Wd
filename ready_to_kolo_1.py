# from file zadania.pdf
# to tn input task number as usual

from math import e, log2, log, cos, sin, pi

tn = 5
match tn:
    case 1:  # trig. function args look like in radians
        # for degrees do '*pi/180' for them
        print('(e**4-log2(34))**(1/3) = {:.2f}'.format((e ** 4 - log2(34)) ** (1 / 3)))
        print('(ln20+cos45+e)**(1/3) = {:.2f}'.format((log(20, e) + cos(45) + e) ** (1 / 3)))
        print('(log3(20)+sin(45)*5/8)**(1/4) = {:.2f}'.format((log(20, 3) + sin(45) * 5 / 8) ** (1 / 4)))
        print('log3(23)+(sin(34)+5)**(1/3) = {:.2f}'.format(log(23, 3) + (sin(34) + 5) ** (1 / 3)))
        print('(log2(32)+pi+sin(56))**(1/4) = {:.2f}'.format((log2(32) + pi + sin(56)) ** (1 / 4)))
    case 2:
        def draw_tower(height):
            try:
                if int(height) > 10:
                    print('Build yourself a tower more than 10 stories high.')
                else:
                    for i in range(int(height)):
                        for j in range(i + 1):
                            print('A', sep='', end='')
                        print()
            except ValueError:
                print('No number - no tower. Bye')


        height = input("Enter tower height in (no more than 10) ")
        draw_tower(height)
    case 3:
        def draw_pyramid(height):
            try:
                if int(height) > 10:
                    print('Build yourself a pyramid more than 10 stories high.')
                else:
                    for i in range(int(height)):
                        for j in range(i + int(height)):
                            if j < int(height) - 1 - i:
                                print(' ', sep='', end='')
                            else:
                                print('A', sep='', end='')
                        print()
            except ValueError:
                print('No number - no pyramid. Bye')


        height = input("Enter pyramid height in (no more than 10) ")
        draw_pyramid(height)
    # case 4:
    # some examples / notes if necessary
    # random() gets random float from [0, 1) interval
    case 5:
        from random import random
        from numpy import ones, zeros

        def row_sums_from_random_matrix(n):
            random_matrix = -ones((n, n))
            row_sums = zeros(n)
            for i in range(n):
                for j in range(n):
                    random_matrix[i, j] = random()
                    row_sums[i] += random_matrix[i, j]
            # print(random_matrix)  # for checking
            return row_sums
        print(row_sums_from_random_matrix(5))
