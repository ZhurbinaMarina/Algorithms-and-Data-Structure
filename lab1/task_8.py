import time

t_start = time.perf_counter()
_min = - 10 ** 9
_max = 10 ** 9
n_min = 3
n_max = 5000
f = open('input_8.txt')
n = int(f.readline())
if n_min <= n <= n_max:
    s = list(map(int, f.readline().split()))
    flag = True
    for el in s:
        if not (_min < el < _max):
            flag = False
    if flag:
        f_output = open('output_8.txt', 'w')
        for i in range(0, len(s) - 1):
            ind = i
            for j in range(i + 1, len(s)):
                if s[j] < s[ind]:
                    ind = j
            if i != ind:
                s[i], s[ind] = s[ind], s[i]
                f_output.write(f'Swap elements at indices {i + 1} and {ind + 1}.\n')
        f_output.write('No more swaps needed.')
        t_stop = time.perf_counter()
        if t_stop - t_start <= 1:
            print("Время выполнения:", t_stop - t_start, 'секунд')
        else:
            print("Превышено время выполнения:", t_stop - t_start, 'секунд')
    else:
        f_output = open('output_8.txt', 'w')
        f_output.write('Введены некоректные данные')
else:
    f_output = open('output_8.txt', 'w')
    f_output.write('Введены некоректные данные')
f.close()
f_output.close()
