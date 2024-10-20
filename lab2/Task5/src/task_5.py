from time import time


def popular_elem(a, start, end):
    if start == end:
        return a[end]
    mid = (start + end) // 2
    left = popular_elem(a, start, mid)
    right = popular_elem(a, mid + 1, end)

    if left == right:
        return left
    left_count = sum(1 for i in range(start, end + 1) if a[i] == left)
    right_count = sum(1 for i in range(start, end + 1) if a[i] == right)

    return left if left_count > right_count else right


t_start = time()
with open("input_5.txt") as f:
    n = int(f.readline())
    if not (1 <= n <= 10 ** 5):
        with open('output_5.txt', 'wt') as g:
            g.write('Введены некорректные данные')
        exit()

    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            with open('output_5.txt', 'wt') as g:
                g.write('Введены некорректные данные')
            exit()

    answ = popular_elem(a, 0, n - 1)
    print(answ)
    with open('output_5.txt', 'wt') as g:
        if a.count(answ) > n / 2:
            g.write('1')
        else:
            g.write('0')

t_stop = time()
if t_stop - t_start <= 2:
    print("Время выполнения:", t_stop - t_start, 'секунд')
else:
    print("Превышено время выполнения:", t_stop - t_start, 'секунд')
