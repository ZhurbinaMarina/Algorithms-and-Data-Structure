from time import time


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        a_left = a[:mid]
        a_right = a[mid:]
        if len(a_left) > 1:
            a_left = merge_sort(a_left)
        if len(a_right) > 1:
            a_right = merge_sort(a_right)

        return merge(a_left, a_right)


def merge(a_left, a_right):
    a = [0] * (len(a_left) + len(a_right))

    a_left.append(10 ** 10)
    a_right.append(10 ** 10)
    i, j = 0, 0
    for k in range(len(a)):
        if a_left[i] <= a_right[j]:
            a[k] = a_left[i]
            i += 1
        else:
            a[k] = a_right[j]
            j += 1

    return a


t_start = time()
with open("input_1.txt") as f:
    n = int(f.readline())
    if not (1 <= n <= 2 * 10 ** 4):
        with open('output_1.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            with open('output_1.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    a = merge_sort(a)
    with open('output_1.txt', 'wt') as g:
        g.write(' '.join([str(elem) for elem in a]))

t_stop = time()
if t_stop - t_start <= 2:
    print("Время выполнения:", t_stop - t_start, 'секунд')
else:
    print("Превышено время выполнения:", t_stop - t_start, 'секунд')
