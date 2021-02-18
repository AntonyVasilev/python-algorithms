"""
В диапазоне натуральных чисел от 2 до заданного числа определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

import cProfile


def multiples(n):
    result_list = [0] * 8

    for num in range(2, n + 1):
        for i in range(2, 10):
            if num % i == 0:
                result_list[i - 2] += 1

    return result_list


# mult_list = multiples(100)
# for i, num in enumerate(mult_list, start=2):
#     print(f'Количество чисел кратных {i}: {num}')

# "task_1_v2.multiples(100)"
# 1000 loops, best of 5: 72.5 usec per loop

# "task_1_v2.multiples(500)"
# 1000 loops, best of 5: 368 usec per loop

# "task_1_v2.multiples(10000)"
# 1000 loops, best of 5: 7.56 msec per loop

# "task_1_v2.multiples(100000)"
# 1000 loops, best of 5: 75.6 msec per loop

# cProfile.run('multiples(100)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1_v2.py:9(multiples)

# cProfile.run('multiples(500)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1_v2.py:9(multiples)

# cProfile.run('multiples(10000)')
# 4 function calls in 0.008 seconds
# 1    0.008    0.008    0.008    0.008 task_1_v2.py:9(multiples)

# cProfile.run('multiples(10000)')
# 4 function calls in 0.008 seconds
# 1    0.008    0.008    0.008    0.008 task_1_v2.py:9(multiples)
