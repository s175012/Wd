# tasks from file lab1.pdf
# type task number to variable below then run
import math

task_number = 1
# 'switch' below
match task_number:
    case 1:
        string_1, str_2 = 'naps', 'tH3.$tH'
        int_1, integer_2 = 1, -50
        floating_point_1, float_2 = 15.9654, 85.0
        complex_1, com_2 = 515 + 46j, -5.6 - 45.02j
        print(string_1, str_2, '\n', int_1, integer_2)
        print(floating_point_1, float_2)
        print(complex_1, com_2)
    case 2:  # considering basic ar. ops as +, -, *, /
        a, b = 1, 2
        do = a+b
        od = a-b
        mn = a*b
        dz = a/b
        print('a=', a, 'b=', b, 'a+b=', do, 'a-b=', od)
        print('a*b=', mn, 'a/n=', dz)
    case 3:
        a, b = 2, 3
        print('a=', a, 'b=', b)
        a += b
        print('a+=b=', a)
        a -= b
        print('a-=b=', a)
        a *= b
        print('a*=b=', a)
        a /= b  # a got cast to float
        print('a/=b=', a)
        a **= b
        print('a=a**=b=', a)
        a %= b
        print('a%=b=', a)
    case 4:
        e = math.e**10
        print("e**10=", e)
        hr = (math.log(5)+math.sin(8)**2)**(1/6)
        print('(ln5+(sin8)**2)**(1/6)=', hr)
        f = math.floor(3.55)
        print('floor(3.55)=', f)
        c = math.ceil(4.8)
        print('ceil(4.8)=', c)
    case 5:  # since repo is public, name shall stay unreal
        i = 'GRZEGORZ'
        n = 'BRZĘCZYSZCZYKIEWICZ'
        print(i, n)
        i = i.capitalize()
        n = n.capitalize()
        print(i, n)
    case 6:  # used 'I really like you' by Carly Rae Jepsen
        f = 'I really, really, really, really, really, really like you'
        a = f.count('really')
        print(f, '\nreally exists', a, 'times in the fragment')
    case 7:
        n = 'han984'
        print(n, '\n2nd char', n[1], 'last char', n[len(n)-1])
    case 8:
        f = 'I really, really, really, really, really, really like you'
        g = f.split()  # might call for extermination of comas
        print(f, '\nsplit:', g)
    case 9:
        s = 'some'
        f = 1.0
        h = hex(26)
        print('string: {chars}'.format(chars=s))
        print('float: {:.2f}'.format(f))
        print('hexadecimal: {hexa}'.format(hexa=h))