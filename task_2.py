"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque
from math import pow


def add_digits(hex_list):
    len_0 = len(hex_list[0])
    len_1 = len(hex_list[1])

    if len_0 != len_1:
        if len_0 > len_1:
            add_len = len_0 - len_1
            hex_list[1].extendleft(['0'] * add_len)
        else:
            add_len = len_1 - len_0
            hex_list[0].extendleft(['0'] * add_len)


def is_hex_number(num_list):
    hex_digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = True

    for digit in num_list:
        if digit not in hex_digits_list:
            result = False
            break
    return result


def hex_sum(hex_list):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    opposite_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_num_1 = hex_list[0]
    hex_num_2 = hex_list[1]
    hex_num_1.reverse()
    hex_num_2.reverse()
    result = deque([])
    add_digit = 0
    for j in range(len(hex_num_1)):
        spam = hex_dict[hex_num_1[j]] + hex_dict[hex_num_2[j]] + add_digit
        if spam < 16:
            result.appendleft(opposite_hex_dict[spam])
            add_digit = 0
        else:
            result.appendleft(opposite_hex_dict[spam - 16])
            add_digit = 1

    if add_digit == 1:
        result.appendleft('1')
    return result


def hex_to_int(hex_num):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = 0
    temp_list = hex_num.copy()
    temp_list.reverse()
    for j, digit in enumerate(temp_list):
        if digit.isdigit():
            result += int(digit) * pow(16, j)
        else:
            result += hex_dict[digit] * pow(16, j)
    return int(result)


def int_to_hex(int_num):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = []

    while int_num >= 16:
        spam = int_num % 16
        if spam < 10:
            result.append(str(spam))
        else:
            result.append(hex_dict[spam])
        int_num //= 16

    if int_num < 10:
        result.append(str(int_num))
    else:
        result.append(hex_dict[int_num])

    result.reverse()
    return result


hex_nums = []

user_num_1 = 'a2'
user_num_2 = 'c4f'

hex_nums.append(deque(user_num_1.upper()))
hex_nums.append(deque(user_num_2.upper()))
#
# num_1 = hex_to_int(hex_nums[0])
# num_2 = hex_to_int(hex_nums[1])

# for i in range(2):
#     user_num = input(f'Введите {i + 1} шестнадцатеричное число: ')
#     hex_nums.append(deque(user_num.upper()))

add_digits(hex_nums)

print(hex_nums)


print(hex_sum(hex_nums))


# print(int_to_hex(hex_to_int(hex_nums[0]) + hex_to_int(hex_nums[1])))
# print(int_to_hex(hex_to_int(hex_nums[0]) * hex_to_int(hex_nums[1])))




