from time import time

cnt = 0


def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)


def merge(a, left, mid, right):
    global cnt
    a_l = a[left:mid + 1] + [10 ** 10]
    a_r = a[mid + 1:right + 1] + [10 ** 10]

    i, j = 0, 0
    for k in range(left, right + 1):
        if a_l[i] <= a_r[j]:
            a[k] = a_l[i]
            i += 1
        else:
            a[k] = a_r[j]
            j += 1
            cnt += len(a_l) - i - 1


t_start = time()
with open("input_3.txt") as f:
    n = int(f.readline())
    if not (1 <= n <= 10 ** 5):
        with open('output_3.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            with open('output_3.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    merge_sort(a, 0, len(a) - 1)
    with open('output_3.txt', 'wt') as g:
        g.write(str(cnt))

t_stop = time()
if t_stop - t_start <= 2:
    print("Время выполнения:", t_stop - t_start, 'секунд')
else:
    print("Превышено время выполнения:", t_stop - t_start, 'секунд')
