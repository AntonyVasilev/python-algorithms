"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

matrix = [[0] * 5 for _ in range(5)]
min_num_list = [10] * 5
max_num = 0

for i in range(5):
    for j in range(5):
        matrix[i][j] = randint(0, 10)
        if matrix[i][j] < min_num_list[j]:
            min_num_list[j] = matrix[i][j]

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

print('-' * 30)
for num in min_num_list:
    print(f'{num:>5}', end='')
    if num > max_num:
        max_num = num

print(f'\n\nМаксимальное число: {max_num}')


