"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint

num_list = [randint(0, 9) for _ in range(10)]
print(f'Исходный массив: {num_list}')

result_min_list = []

for i in range(2):
    min_num = 10

    for num in num_list:
        if num < min_num:
            min_num = num

    pop_num = num_list.pop(num_list.index(min_num))
    result_min_list.append(pop_num)

print(f'Два наименьших числа в массиве: {result_min_list}')
