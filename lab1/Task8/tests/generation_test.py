import random

n = 5000
_min = -10 ** 9
_max = 10 ** 9
s = [str(random.randint(_min, _max)) for i in range(n)]
with open('../src/input_8.txt', 'wt') as f:
    f.write(str(n) + '\n')
    f.write(' '.join(s))
