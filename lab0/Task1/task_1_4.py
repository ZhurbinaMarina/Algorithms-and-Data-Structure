f = open('input_4.txt')
a, b = map(int, f.readline().split())
f_output = open('output_4.txt', 'w')
f_output.write(str(a + b ** 2))
f.close()
f_output.close()
