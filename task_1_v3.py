"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.

import sys


def is_hex_number(num_list):
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = True

    for digit in num_list:
        if digit.upper() not in hex_list:
            result = False
            break
    return result


def show_size(obj, level=0):
    result = sys.getsizeof(obj)
    size = 0
    print('\t' * level, f'type= {obj.__class__}, size= {sys.getsizeof(obj)}, object= {obj}')

    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for item in obj.items():
                size = show_size(item, level + 1)
                result += size
        elif not isinstance(obj, str):
            for el in obj:
                size = show_size(el, level + 1)
                result += size

    return result


hex_nums = []
stop_sign = False

for i in range(2):
    user_num = input(f'Введите {i + 1} шестнадцатеричное число: ')
    if is_hex_number(user_num):
        hex_nums.append(user_num.upper())
    else:
        stop_sign = True
        break

if not stop_sign:
    num_1 = int(hex_nums[0], base=16)
    num_2 = int(hex_nums[1], base=16)
    nums_sum = num_1 + num_2
    nums_mult = num_1 * num_2
    print(f'Сумма: {list(hex(nums_sum).upper())}')
    print(f'Произведение: {list(hex(nums_mult).upper())}')

# print(sys.version, sys.platform)
# 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] win32
#     print(show_size(hex_nums))
    # print(sys.getsizeof(hex_nums[0]))
    # print(sys.getsizeof(hex_nums[1]))
    # print((sys.getsizeof(num_1)))
    # print((sys.getsizeof(num_2)))
    # print((sys.getsizeof(nums_sum)))
    # print((sys.getsizeof(nums_mult)))

overall_size = 0
var_list = [el for el in dir() if '__' not in el]
# print(globals()[var_list[0]])
for var in var_list:
    print('*' * 50)
    current_size = show_size(globals()[var])
    overall_size += current_size

print('*' * 50)
print(f'Общая память, занимаемая переменными: {overall_size}')
