from time import time


def merge_sort(a, left, right, output_file):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid, output_file)
        merge_sort(a, mid + 1, right, output_file)
        merge(a, left, mid, right, output_file)


def merge(a, left, mid, right, output_file):
    a_l = a[left:mid + 1] + [10 ** 100]
    a_r = a[mid + 1:right + 1] + [10 ** 100]

    i, j = 0, 0
    for k in range(left, right + 1):
        if a_l[i] <= a_r[j]:
            a[k] = a_l[i]
            i += 1
        else:
            a[k] = a_r[j]
            j += 1

    output_file.write(f'{left + 1} {right + 1} {a[left]} {a[right]}\n')


t_start = time()
with open("input_2.txt") as f:
    n = int(f.readline())
    if not (1 <= n <= 10 ** 5):
        with open('output_2.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            with open('output_2.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    g =  open('output_2.txt', 'wt')
    g.write("")
    merge_sort(a, 0, len(a) - 1, g)
    g.write(' '.join([str(elem) for elem in a]))
    g.close()

t_stop = time()
if t_stop - t_start <= 2:
    print("Время выполнения:", t_stop - t_start, 'секунд')
else:
    print("Превышено время выполнения:", t_stop - t_start, 'секунд')
