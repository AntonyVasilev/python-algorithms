"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque
from math import pow

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
opposite_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                     10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# Добавляет недостающее количество нулей перед числом с меньшим количеством разрядов, чтобы их число одинаковым
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


# Проверяет, все ли символы в введенных числах соответствуют допустимым в шестнадцатеричной системе счисления
def is_hex_number(num_list):
    result = True

    for digit in num_list:
        if digit not in hex_dict.keys():
            result = False
            break
    return result


# Расчет суммы двух шестнадцатеричных чисел
def hex_sum(hex_list):
    hex_num_1 = hex_list[0].copy()
    hex_num_2 = hex_list[1].copy()
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
        result.appendleft(str(add_digit))
    return result


# Расчет произведения двух шестнадцатеричных чисел
def hex_multiple(hex_list):
    hex_num_1 = hex_list[0].copy()
    hex_num_2 = hex_list[1].copy()
    hex_num_1.reverse()
    hex_num_2.reverse()
    result_list = []
    add_digit = 0

    for i in range(len(hex_num_1)):
        temp_list = deque([])
        for j in range(len(hex_num_2)):
            if hex_num_2[i] == '0':     # Если во втором числе присутствует цифра 0, то для нее расчет не производится
                break
            spam = hex_dict[hex_num_1[j]] * hex_dict[hex_num_2[i]] + add_digit
            if spam < 16:
                temp_list.appendleft(opposite_hex_dict[spam])
                add_digit = 0
            else:
                temp_list.appendleft(opposite_hex_dict[spam % 16])
                add_digit = spam // 16

        if hex_num_2[i] != '0':     # Также условие для обработки цифры 0
            if add_digit > 0:
                temp_list.appendleft(opposite_hex_dict[add_digit])
                temp_list.extendleft(['0'] * (len(hex_num_1) - i - 2))
                add_digit = 0
            else:
                temp_list.extendleft(['0'] * (len(hex_num_1) - i - 1))
            temp_list.extend(['0'] * i)
            result_list.append(temp_list)

    result = hex_sum([result_list[0], result_list[1]])
    if len(result_list) > 2:
        for i in range(2, len(hex_num_1)):
            result = hex_sum([result, result_list[i]])

    if add_digit > 0:
        result.appendleft(str(add_digit))
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

for i in range(2):
    user_num = input(f'Введите {i + 1} шестнадцатеричное число: ')
    hex_nums.append(deque(user_num.upper()))

add_digits(hex_nums)

print(hex_nums, sep='\n')

# Вариант 1
# Сумма и произведение производится "в столбик" в соответствии с методикой из расчета
print(f'Сумма 1: {list(hex_sum(hex_nums))}')
print(f'Произведение 1: {list(hex_multiple(hex_nums))}')

# Вариант 2
# Сначала числа переводятся в десятичную систему счисления, в ней производятся сложение и умножение соответственно,
# а потом результат переводится обратно в шестнадцатеричную систему счисления
print(f'Сумма 2: {int_to_hex(hex_to_int(hex_nums[0]) + hex_to_int(hex_nums[1]))}')
print(f'Произведение 2: {int_to_hex(hex_to_int(hex_nums[0]) * hex_to_int(hex_nums[1]))}')
