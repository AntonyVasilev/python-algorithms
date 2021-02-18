"""
В диапазоне натуральных чисел от 2 до заданного числа определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

import cProfile


def multiples(n):
    result_dict = {key: [] for key in range(2, 10)}

    for num in range(2, n + 1):
        if num % 2 == 0:
            result_dict[2].append(num)
        if num % 3 == 0:
            result_dict[3].append(num)
        if num % 4 == 0:
            result_dict[4].append(num)
        if num % 5 == 0:
            result_dict[5].append(num)
        if num % 6 == 0:
            result_dict[6].append(num)
        if num % 7 == 0:
            result_dict[7].append(num)
        if num % 8 == 0:
            result_dict[8].append(num)
        if num % 9 == 0:
            result_dict[9].append(num)

    return result_dict

#
# mult_dict = multiples(100)
# for i in range(2, 10):
#     print(f'Количество чисел кратных {i}: {len(mult_dict[i])}')


# "task_1_v1.multiples(100)"
# 1000 loops, best of 5: 45.5 usec per loop

# "task_1_v1.multiples(500)"
# 1000 loops, best of 5: 229 usec per loop

# "task_1_v1.multiples(10000)"
# 1000 loops, best of 5: 4.59 msec per loop

# "task_1_v1.multiples(100000)"
# 1000 loops, best of 5: 46.7 msec per loop

# cProfile.run('multiples(100)')
# 186 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1_v1.py:9(multiples)
# 181    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('multiples(500)')
# 917 function calls in 0.000 seconds
# 1    0.001    0.001    0.001    0.001 task_1_v1.py:9(multiples)
# 912    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('multiples(10000)')
# 18293 function calls in 0.007 seconds
# 1    0.006    0.006    0.007    0.007 task_1_v1.py:9(multiples)
# 18288    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

# cProfile.run('multiples(100000)')
# 182900 function calls in 0.073 seconds
# 1    0.060    0.060    0.072    0.072 task_1_v1.py:9(multiples)
# 182895    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}
