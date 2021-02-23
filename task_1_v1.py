"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.

from collections import deque
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
        if digit.upper() not in hex_dict.keys():
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


hex_nums = []
stop_sign = False

for i in range(2):
    user_num = input(f'Введите {i + 1} шестнадцатеричное число: ')
    if is_hex_number(user_num):
        hex_nums.append(deque(user_num.upper()))
    else:
        print('Введено не шестнадцатеричное число.')
        stop_sign = True
        break

if not stop_sign:
    add_digits(hex_nums)

    print(hex_nums)
    print(f'Сумма 1: {list(hex_sum(hex_nums))}')
    print(f'Произведение 1: {list(hex_multiple(hex_nums))}')


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
 type= <class 'function'>, size= 136, object= <function add_digits at 0x0000021E44B1F4C0>
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
 type= <class 'function'>, size= 136, object= <function hex_multiple at 0x0000021E44B1F160>
**************************************************
 type= <class 'list'>, size= 88, object= [deque(['A', 'F', 'F']), deque(['0', 'D', 'D'])]
	 type= <class 'collections.deque'>, size= 624, object= deque(['A', 'F', 'F'])
		 type= <class 'str'>, size= 50, object= A
		 type= <class 'str'>, size= 50, object= F
		 type= <class 'str'>, size= 50, object= F
	 type= <class 'collections.deque'>, size= 624, object= deque(['0', 'D', 'D'])
		 type= <class 'str'>, size= 50, object= 0
		 type= <class 'str'>, size= 50, object= D
		 type= <class 'str'>, size= 50, object= D
**************************************************
 type= <class 'function'>, size= 136, object= <function hex_sum at 0x0000021E44B1F3A0>
**************************************************
 type= <class 'int'>, size= 28, object= 1
**************************************************
 type= <class 'function'>, size= 136, object= <function is_hex_number at 0x0000021E44B1F430>
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
 type= <class 'int'>, size= 28, object= 7768
**************************************************
 type= <class 'function'>, size= 136, object= <function show_size at 0x0000021E4222D820>
**************************************************
 type= <class 'bool'>, size= 24, object= False
**************************************************
 type= <class 'module'>, size= 72, object= <module 'sys' (built-in)>
**************************************************
 type= <class 'str'>, size= 51, object= dd
**************************************************
Общая память, занимаемая переменными: 8079 байт
"""