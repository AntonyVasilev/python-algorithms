"""
В диапазоне натуральных чисел от 2 до заданного числа определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

import cProfile


def multiples(n):
    result_list = [0] * 8

    for num in range(2, n + 1):
        if num % 2 == 0:
            result_list[0] += 1
        if num % 3 == 0:
            result_list[1] += 1
        if num % 4 == 0:
            result_list[2] += 1
        if num % 5 == 0:
            result_list[3] += 1
        if num % 6 == 0:
            result_list[4] += 1
        if num % 7 == 0:
            result_list[5] += 1
        if num % 8 == 0:
            result_list[6] += 1
        if num % 9 == 0:
            result_list[7] += 1

    return result_list


# mult_list = multiples(100)
# for i in range(2, 10):
#     print(f'Количество чисел кратных {i}: {mult_list[i - 2]}')

# "task_1_v3.multiples(100)"
# 1000 loops, best of 5: 43.9 usec per loop

# "task_1_v3.multiples(500)"
# 1000 loops, best of 5: 218 usec per loop

# "task_1_v3.multiples(10000)"
# 1000 loops, best of 5: 4.57 msec per loop

# "task_1_v3.multiples(100000)"
# 1000 loops, best of 5: 46.8 msec per loop

# cProfile.run('multiples(100)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1_v3.py:9(multiples)

# cProfile.run('multiples(500)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1_v3.py:9(multiples)

# cProfile.run('multiples(10000)')
# 4 function calls in 0.005 seconds
# 1    0.005    0.005    0.005    0.005 task_1_v3.py:9(multiples)

# cProfile.run('multiples(100000)')
# 4 function calls in 0.047 seconds
# 1    0.047    0.047    0.047    0.047 task_1_v3.py:9(multiples)


"""
У всех вариантов кода наблюдается линейная сложность алгоритмов. 
По результатам теста timeit в 1 и 3 вариантах скорость выполнения задачи практически идентична, 
а вот во 2 варианте код выполняется в 1,6 раза дольше. 
По результатам cProfile во 2 и 3 вариантах функции вызываются по 1 разу, а в 1 варианте многократно вызывается функция 
append. Это занимает в 1,5 раза больше времени по сравнению с 3 вариантом.
На основании полученных результатов тестирования 3-х вариантов кода я пришел к выводу, что лучшим вариантов является 
task_1_v3.py.    
"""