import time

t_start = time.perf_counter()
n_min = 1
n_max = 10 ** 5
f = open('input_10.txt')
n = int(f.readline())
if n_min <= n <= n_max:
    s = f.readline()
    ord_A = ord("A")
    a = [0] * (ord("Z") - ord_A + 1)
    for elem in s:
        a[ord(elem) - ord_A] += 1
    left_side = ''
    center = ''
    for i in range(len(a)):
        ch, cnt = chr(i + ord_A), a[i]
        h = ch * (cnt // 2)
        left_side += h
        if center == "" and cnt % 2 == 1:
            center = ch
    f_output = open('output_10.txt', 'w')
    f_output.write(left_side + center + left_side[::-1])
    t_stop = time.perf_counter()
    if t_stop - t_start <= 1:
        print("Время выполнения:", t_stop - t_start, 'секунд')
    else:
        print("Превышено время выполнения:", t_stop - t_start, 'секунд')
else:
    f_output = open('output_10.txt', 'w')
    f_output.write('Введены некоректные данные')
f.close()
f_output.close()
