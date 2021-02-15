"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

frequency_dict = {i: 0 for i in range(10)}
num_list = [randint(0, 5) for _ in range(20)]
max_frequency = [0, 0]

for num in num_list:
    frequency_dict[num] += 1

for key, value in frequency_dict.items():
    if value > max_frequency[1]:
        max_frequency[0] = key
        max_frequency[1] = value

print(f'Исходный массив чисел: {num_list}')
print(f'Наиболее часто встречающееся число: {max_frequency[0]}')
