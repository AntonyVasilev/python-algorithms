"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

num_list = [randint(0, 99) for _ in range(10)]

max_num = 0
min_num = 100

for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f'Исходный список: {num_list}')
print(f'Максимальный элемент: {max_num}, минимальный элемент: {min_num}')

max_num_idx = num_list.index(max_num)
min_num_idx = num_list.index(min_num)

num_list[min_num_idx], num_list[max_num_idx] = num_list[max_num_idx], num_list[min_num_idx]
print(num_list)
