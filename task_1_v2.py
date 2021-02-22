"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.

from collections import deque
from math import pow

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
opposite_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                     10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# Проверяет, все ли символы в введенных числах соответствуют допустимым в шестнадцатеричной системе счисления
def is_hex_number(num_list):
    result = True

    for digit in num_list:
        if digit.upper() not in hex_dict.keys():
            result = False
            break
    return result


# Функция перевода числа из шестнадцатеричной системы счисления в десятичную
def hex_to_int(hex_num):
    result = 0
    temp_list = hex_num.copy()
    temp_list.reverse()

    for j, digit in enumerate(temp_list):
        if digit.isdigit():
            result += int(digit) * pow(16, j)
        else:
            result += hex_dict[digit] * pow(16, j)
    return int(result)


# Функция перевода числа из десятичной системы счисления в шестнадцатеричную
def int_to_hex(int_num):
    result = []

    while int_num >= 16:
        spam = int_num % 16
        if spam < 10:
            result.append(str(spam))
        else:
            result.append(opposite_hex_dict[spam])
        int_num //= 16

    if int_num < 10:
        result.append(str(int_num))
    else:
        result.append(opposite_hex_dict[int_num])

    result.reverse()
    return result


hex_nums = []
stop_sign = False

for i in range(2):
    user_num = input(f'Введите {i + 1} шестнадцатеричное число: ')
    if is_hex_number(user_num):
        hex_nums.append(deque(user_num.upper()))
    else:
        stop_sign = True
        break

if not stop_sign:
    print(hex_nums)

    print(f'Сумма 2: {int_to_hex(hex_to_int(hex_nums[0]) + hex_to_int(hex_nums[1]))}')
    print(f'Произведение 2: {int_to_hex(hex_to_int(hex_nums[0]) * hex_to_int(hex_nums[1]))}')
