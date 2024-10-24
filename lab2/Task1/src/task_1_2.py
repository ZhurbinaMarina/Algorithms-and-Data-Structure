# -*- coding: utf-8 -*-
import time

t_start = time.perf_counter()
_min = - 10 ** 9
_max = 10 ** 9
n_min = 1
n_max = 2 * 10 ** 4
f = open('input_1.txt')
n = int(f.readline())
if n_min <= n <= n_max:
    s = list(map(int, f.readline().split()))
    flag = True
    for el in s:
        if not (_min <= el <= _max):
            flag = False
    if flag:
        for i in range(1, len(s)):
            a = s[i]
            j = i - 1
            while j >= 0 and a < s[j]:
                s[j + 1] = s[j]
                j = j - 1
            s[j + 1] = a
        f_output = open('output_1.txt', 'w')
        f_output.write(' '.join(map(str, s)))
        t_stop = time.perf_counter()
        if t_stop - t_start <= 2:
            print("Время выполнения:", t_stop - t_start, 'секунд')
        else:
            print("Превышено время выполнения:", t_stop - t_start, 'секунд')
    else:
        f_output = open('output_1.txt', 'w')
        f_output.write('Введены некоректные данные')
else:
    f_output = open('output_1.txt', 'w')
    f_output.write('Введены некоректные данные')
f.close()
f_output.close()
