n = 10 ** 5
_min = -10 ** 9
_max = 10 ** 9
s = [str(i) for i in range(-10 ** 9, -10 ** 9 + n)]
s.reverse()
with open('../src/input_3.txt', 'wt') as f:
    f.write(str(len(s)) + '\n')
    f.write(' '.join(s))
