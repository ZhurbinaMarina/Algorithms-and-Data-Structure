from time import time


def binary_search(a, value):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == a[mid]:
            return mid

        if value > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


t_start = time()
with open("input_4.txt") as f:
    n = int(f.readline())
    if not (1 <= n <= 10 ** 5):
        with open('output_4.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    a = list(map(int, f.readline().split()))
    for elem in a:
        if not (1 <= elem <= 10 ** 9):
            with open('output_4.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    k = int(f.readline())
    if not (1 <= k <= 10 ** 5):
        with open('output_4.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    b = list(map(int, f.readline().split()))
    for elem in b:
        if not (1 <= elem <= 10 ** 9):
            with open('output_4.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    res = []
    for elem in b:
        res.append(str(binary_search(a, elem)))
    with open('output_4.txt', 'wt') as g:
        g.write(' '.join([str(elem) for elem in res]))

t_stop = time()
if t_stop - t_start <= 2:
    print("Время выполнения:", t_stop - t_start, 'секунд')
else:
    print("Превышено время выполнения:", t_stop - t_start, 'секунд')
