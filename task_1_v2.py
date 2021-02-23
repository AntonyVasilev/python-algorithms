"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.

from collections import deque
from math import pow
import sys

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
opposite_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                     10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def show_size(obj, level=0):
    result = sys.getsizeof(obj)
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


overall_size = 0
var_list = [el for el in dir() if '__' not in el and el != 'deque']

for var in var_list:
    print('*' * 50)
    current_size = show_size(globals()[var])
    overall_size += current_size

print('*' * 50)
print(f'Общая память, занимаемая переменными: {overall_size} байт')


# print(sys.version, sys.platform)
# 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)] win32
#     print(show_size(hex_nums))

"""
**************************************************
 type= <class 'dict'>, size= 640, object= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                                            '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
	 type= <class 'tuple'>, size= 56, object= ('0', 0)
		 type= <class 'str'>, size= 50, object= 0
		 type= <class 'int'>, size= 24, object= 0
	 type= <class 'tuple'>, size= 56, object= ('1', 1)
		 type= <class 'str'>, size= 50, object= 1
		 type= <class 'int'>, size= 28, object= 1
	 type= <class 'tuple'>, size= 56, object= ('2', 2)
		 type= <class 'str'>, size= 50, object= 2
		 type= <class 'int'>, size= 28, object= 2
	 type= <class 'tuple'>, size= 56, object= ('3', 3)
		 type= <class 'str'>, size= 50, object= 3
		 type= <class 'int'>, size= 28, object= 3
	 type= <class 'tuple'>, size= 56, object= ('4', 4)
		 type= <class 'str'>, size= 50, object= 4
		 type= <class 'int'>, size= 28, object= 4
	 type= <class 'tuple'>, size= 56, object= ('5', 5)
		 type= <class 'str'>, size= 50, object= 5
		 type= <class 'int'>, size= 28, object= 5
	 type= <class 'tuple'>, size= 56, object= ('6', 6)
		 type= <class 'str'>, size= 50, object= 6
		 type= <class 'int'>, size= 28, object= 6
	 type= <class 'tuple'>, size= 56, object= ('7', 7)
		 type= <class 'str'>, size= 50, object= 7
		 type= <class 'int'>, size= 28, object= 7
	 type= <class 'tuple'>, size= 56, object= ('8', 8)
		 type= <class 'str'>, size= 50, object= 8
		 type= <class 'int'>, size= 28, object= 8
	 type= <class 'tuple'>, size= 56, object= ('9', 9)
		 type= <class 'str'>, size= 50, object= 9
		 type= <class 'int'>, size= 28, object= 9
	 type= <class 'tuple'>, size= 56, object= ('A', 10)
		 type= <class 'str'>, size= 50, object= A
		 type= <class 'int'>, size= 28, object= 10
	 type= <class 'tuple'>, size= 56, object= ('B', 11)
		 type= <class 'str'>, size= 50, object= B
		 type= <class 'int'>, size= 28, object= 11
	 type= <class 'tuple'>, size= 56, object= ('C', 12)
		 type= <class 'str'>, size= 50, object= C
		 type= <class 'int'>, size= 28, object= 12
	 type= <class 'tuple'>, size= 56, object= ('D', 13)
		 type= <class 'str'>, size= 50, object= D
		 type= <class 'int'>, size= 28, object= 13
	 type= <class 'tuple'>, size= 56, object= ('E', 14)
		 type= <class 'str'>, size= 50, object= E
		 type= <class 'int'>, size= 28, object= 14
	 type= <class 'tuple'>, size= 56, object= ('F', 15)
		 type= <class 'str'>, size= 50, object= F
		 type= <class 'int'>, size= 28, object= 15
**************************************************
 type= <class 'list'>, size= 88, object= [deque(['A', 'F', 'F']), deque(['D', 'D'])]
	 type= <class 'collections.deque'>, size= 624, object= deque(['A', 'F', 'F'])
		 type= <class 'str'>, size= 50, object= A
		 type= <class 'str'>, size= 50, object= F
		 type= <class 'str'>, size= 50, object= F
	 type= <class 'collections.deque'>, size= 624, object= deque(['D', 'D'])
		 type= <class 'str'>, size= 50, object= D
		 type= <class 'str'>, size= 50, object= D
**************************************************
 type= <class 'function'>, size= 136, object= <function hex_to_int at 0x000002CBFFA4F550>
**************************************************
 type= <class 'int'>, size= 28, object= 1
**************************************************
 type= <class 'function'>, size= 136, object= <function int_to_hex at 0x000002CBFFA4F4C0>
**************************************************
 type= <class 'function'>, size= 136, object= <function is_hex_number at 0x000002CBFE57E820>
**************************************************
 type= <class 'dict'>, size= 640, object= {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 
                                            9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
	 type= <class 'tuple'>, size= 56, object= (0, '0')
		 type= <class 'int'>, size= 24, object= 0
		 type= <class 'str'>, size= 50, object= 0
	 type= <class 'tuple'>, size= 56, object= (1, '1')
		 type= <class 'int'>, size= 28, object= 1
		 type= <class 'str'>, size= 50, object= 1
	 type= <class 'tuple'>, size= 56, object= (2, '2')
		 type= <class 'int'>, size= 28, object= 2
		 type= <class 'str'>, size= 50, object= 2
	 type= <class 'tuple'>, size= 56, object= (3, '3')
		 type= <class 'int'>, size= 28, object= 3
		 type= <class 'str'>, size= 50, object= 3
	 type= <class 'tuple'>, size= 56, object= (4, '4')
		 type= <class 'int'>, size= 28, object= 4
		 type= <class 'str'>, size= 50, object= 4
	 type= <class 'tuple'>, size= 56, object= (5, '5')
		 type= <class 'int'>, size= 28, object= 5
		 type= <class 'str'>, size= 50, object= 5
	 type= <class 'tuple'>, size= 56, object= (6, '6')
		 type= <class 'int'>, size= 28, object= 6
		 type= <class 'str'>, size= 50, object= 6
	 type= <class 'tuple'>, size= 56, object= (7, '7')
		 type= <class 'int'>, size= 28, object= 7
		 type= <class 'str'>, size= 50, object= 7
	 type= <class 'tuple'>, size= 56, object= (8, '8')
		 type= <class 'int'>, size= 28, object= 8
		 type= <class 'str'>, size= 50, object= 8
	 type= <class 'tuple'>, size= 56, object= (9, '9')
		 type= <class 'int'>, size= 28, object= 9
		 type= <class 'str'>, size= 50, object= 9
	 type= <class 'tuple'>, size= 56, object= (10, 'A')
		 type= <class 'int'>, size= 28, object= 10
		 type= <class 'str'>, size= 50, object= A
	 type= <class 'tuple'>, size= 56, object= (11, 'B')
		 type= <class 'int'>, size= 28, object= 11
		 type= <class 'str'>, size= 50, object= B
	 type= <class 'tuple'>, size= 56, object= (12, 'C')
		 type= <class 'int'>, size= 28, object= 12
		 type= <class 'str'>, size= 50, object= C
	 type= <class 'tuple'>, size= 56, object= (13, 'D')
		 type= <class 'int'>, size= 28, object= 13
		 type= <class 'str'>, size= 50, object= D
	 type= <class 'tuple'>, size= 56, object= (14, 'E')
		 type= <class 'int'>, size= 28, object= 14
		 type= <class 'str'>, size= 50, object= E
	 type= <class 'tuple'>, size= 56, object= (15, 'F')
		 type= <class 'int'>, size= 28, object= 15
		 type= <class 'str'>, size= 50, object= F
**************************************************
 type= <class 'int'>, size= 28, object= 7582
**************************************************
 type= <class 'builtin_function_or_method'>, size= 72, object= <built-in function pow>
**************************************************
 type= <class 'function'>, size= 136, object= <function show_size at 0x000002CBFE57E4C0>
**************************************************
 type= <class 'bool'>, size= 24, object= False
**************************************************
 type= <class 'module'>, size= 72, object= <module 'sys' (built-in)>
**************************************************
 type= <class 'str'>, size= 51, object= dd
**************************************************
Общая память, занимаемая переменными: 7965 байт
"""
