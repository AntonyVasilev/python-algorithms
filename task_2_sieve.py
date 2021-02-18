"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
С помощью алгоритма «Решето Эратосфена».
"""
import cProfile


def sieve(n):
    num_count = 0
    sieve_list = [0, 0]
    list_len = 2
    result_list = []
    while num_count < n:
        sieve_list.append(list_len)
        for i in range(2, list_len + 1):
            if sieve_list[i] != 0:
                j = i * 2

                while j < list_len + 1:
                    sieve_list[j] = 0
                    j += i
        result_list = [i for i in sieve_list if i != 0]
        num_count = len(result_list)
        list_len += 1

    return result_list[-1]


# sieve_result = sieve(5)
# print(sieve_result)

# "task_2_sieve.sieve(1)"
# 1000 loops, best of 5: 939 nsec per loop

# "task_2_sieve.sieve(5)"
# 1000 loops, best of 5: 15.7 usec per loop

# "task_2_sieve.sieve(10)"
# 1000 loops, best of 5: 92.7 usec per loop

# "task_2_sieve.sieve(20)"
# 1000 loops, best of 5: 537 usec per loop

# "task_2_sieve.sieve(50)"
# 1000 loops, best of 5: 5.83 msec per loop

# cProfile.run('sieve(1)')
# 7 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_2_sieve.py:22(<listcomp>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('sieve(5)')
# 34 function calls in 0.000 seconds
# 10    0.000    0.000    0.000    0.000 task_2_sieve.py:22(<listcomp>)
# 10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('sieve(10)')
# 88 function calls in 0.000 seconds
# 28    0.000    0.000    0.000    0.000 task_2_sieve.py:22(<listcomp>)
# 28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 28    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('sieve(20)')
# 214 function calls in 0.001 seconds
# 70    0.000    0.000    0.000    0.000 task_2_sieve.py:22(<listcomp>)
# 70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 70    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('sieve(50)')
# 688 function calls in 0.006 seconds
# 228    0.001    0.000    0.001    0.000 task_2_sieve.py:23(<listcomp>)
# 228    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
