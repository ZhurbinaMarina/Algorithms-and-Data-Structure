import random

n = 100000
ord_A = ord('A')
ord_Z = ord('Z')
s = [chr(random.randint(ord_A, ord_Z)) for i in range(n)]
with open('Task10/input_10.txt', 'wt') as f:
    f.write(str(n) + '\n')
    f.write(''.join(s))
