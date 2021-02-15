"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

num_list = [randint(0, 15) for _ in range(10)]
# num_list = []
# for i in range(20):
#     new_num = randint(0, 15)
#     if new_num not in num_list:
#         num_list.append(new_num)
print(f'Исходный массив: {num_list}')

result_sum = 0
max_num = 0
min_num = 10

for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f'минимальное число: {min_num}, максимальное число: {max_num}.')

max_num_idx = num_list.index(max_num)
min_num_idx = num_list.index(min_num)

if max_num_idx > min_num_idx:
    for num in num_list[min_num_idx + 1: max_num_idx]:
        result_sum += num
elif min_num_idx > max_num_idx:
    for num in num_list[max_num_idx + 1: min_num_idx]:
        result_sum += num
else:
    result_sum = 0

print(f'Сумма равна {result_sum}')
