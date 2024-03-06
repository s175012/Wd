# tasks from file lab2.docx
# type task number to variable below then run
import sys
import math

task_number = 8

match task_number:
    case 1:
        z = input("Type a sentence: ")
        print('The sentence consists of', z.count(' ')+1, "words.")
    case 2:
        sys.stdout.write('Type integer a: ')
        a = sys.stdin.readline()
        sys.stdout.write('Type integer b: ')
        b = sys.stdin.readline()
        sys.stdout.write('Type integer c: ')
        c = sys.stdin.readline()
        d = int(a) ** int(b) + int(c)
        print('a**b+c=', d)
    case 3:
        n = input('type sth: ')
        f = 1
        for i in range(math.ceil(len(n))):
            if n[i] != n[len(n)-1-i]:
                f = 0
                print("no palindrome")
                break
        if f:
            print("palindrome")
    case 4:
        n = int(input('type natural number: '))
        f = 1
        for i in range(2, math.floor(math.sqrt(n))):
            if n % i == 0:
                f = 0
                print("divides by", i, "no prime number")
                break
        if f:
            print("prime number")
    case 5:
        n = int(input('type natural number: '))
        m = 1
        for i in range(2, n):
            if n % i == 0:
                m += i
                print(i)
        if m == n:
            print("perfect number")
        else:
            print("sum of dividers", m, "\nno perfect number")
    case 6:
        ns = [5, -12.65]
        print(ns)
        for i in range(len(ns)):
            ns[i] **= 2
        print(ns)
    case 7:
        i = 0
        n = []
        while i < 10:
            t = int(input('Type integer: '))
            if t % 2 == 0:
                n.append(t)
            i += 1
        print(n)
    case 8:
        r = [1, 1, 0, 'dsf', 'hk564', -952.162, 15-5.1j]
        print(r)
        s = {}
        for i in range(len(r)):
            if r[i] in s.keys():
                continue
            w = 1
            for j in range(i + 1, len(r)):
                if r[i] == r[j]:
                    w += 1
            s[r[i]] = w
        print(s)
        # I've established that elements mean keys,
        # since values can only be numeric.
        k = list(s)
        for i in range(len(k)):
            t = type(k[i])
            if t != int and t != complex and t != float:
                s.pop(k[i])
        print(s)
        del k
