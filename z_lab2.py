# tasks from file lab2.pdf
# type task number to variable below then run
import sys
import math

task_number = 1

match task_number:
    case 1:
        sports = ['running', 'swimming', 'skiing']
        print(sports)
        sports.reverse()
        sports.append('disc throwing')
        print(sports)
    case 2:
        shorts = {'yolo': 'you only live once', 'faq': 'frequently asked questions'}
    case 3:
        games = {'pd': 'Pixel Dungeon', '20mtd': '20 minutes till dawn'}
        print(games.keys(), 'There are', len(games), 'here')
    case 4:
        z = input("Type a sentence: ")
        print('A appeared', z.count('a'), "time(s).")
    case 5:
        sys.stdout.write('Type base: ')
        a = sys.stdin.readline()
        sys.stdout.write('Type degree of power: ')
        b = sys.stdin.readline()
        sys.stdout.write('Type extra: ')
        c = sys.stdin.readline()
        d = int(a)**int(b)+int(c)
        print('base**degree+extra=', d)
    case 6:
        nums = input('Type 3 integers separated by " ": ').split(' ')
        for i in range(3):
            nums[i] = int(nums[i])
        if nums[0] > nums[1]:
            if nums[0] > nums[2]:
                print(nums[0], 'is the greatest')
            else:
                print(nums[2], 'is the greatest')
        elif nums[1] > nums[2]:
            print(nums[1], 'is the greatest')
        else:
            print(nums[2], 'is the greatest')
    case 7:
        n = [2, -3.5]
        print(n)
        for i in range(len(n)):
            n[i] **= 2
        print(n)
    case 8:
        i = 0
        n = []
        while i < 10:
            t = int(input('Type integer: '))
            if t % 2 == 0:
                n.append(t)
            i += 1
        print(n)
    case 9:
        n = float(input('type non-negative number: '))
        try:
            s = math.sqrt(n)
        except ValueError:
            print('negative number')
        else:
            print('Square root {:f}='.format(n), s)
