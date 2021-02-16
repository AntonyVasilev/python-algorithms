"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = [[0] * 5 for _ in range(4)]

for i in range(4):
    for j in range(4):
        user_num = int(input(f'Введите число. Строка {i + 1} столбец {j + 1}: '))
        matrix[i][j] = user_num
        matrix[i][4] += matrix[i][j]

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()
