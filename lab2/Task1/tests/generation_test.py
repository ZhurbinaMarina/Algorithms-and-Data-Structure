from random import randint

n = 2 * 10 ** 4
_min = -10 ** 9
_max = 10 ** 9
s = [str(randint(_min, _max)) for _ in range(n)]
s.reverse()
with open('../src/input_1.txt', 'wt') as f:
    f.write(str(len(s)) + '\n')
    f.write(' '.join(s))
