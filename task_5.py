"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

max_negative_num = 0
num_list = [randint(-20, -1) for _ in range(10)]
print(f'Исходный массив: {num_list}')

for num in num_list:
    if num < max_negative_num:
        max_negative_num = num

print(f'Максимальное отрицательное число: {max_negative_num}. Его позиция: {num_list.index(max_negative_num)}')
