from random import randint, shuffle

n = 10 ** 5
_min = 1
_max = 10 ** 9
s = [randint(_min, _max) for _ in range(n)]
s.sort()
s = [str(x) for x in s]

with open('../src/input_4.txt', 'wt') as f:
    f.write(str(n) + '\n')
    f.write(' '.join(s) + '\n')
    f.write(str(n) + '\n')
    shuffle(s)
    f.write(' '.join(s))
