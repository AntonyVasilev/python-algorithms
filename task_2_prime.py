"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Без использования «Решета Эратосфена».
"""
import cProfile


def prime(n):

    if n == 1:
        return 2

    num = 3
    result_list = []
    list_len = 0

    while list_len < n:
        result_list.clear()     # без очистки списка работает не правильно
        for i in range(2, num + 1):
            for j in range(2, i):

                if i % j == 0:
                    break

            else:
                result_list.append(i)

        num += 1
        list_len = len(result_list)

    return result_list[-1]


# prime_num = prime(5)
# print(prime_num)

# "task_2_prime.prime(1)"
# 1000 loops, best of 5: 113 nsec per loop

# "task_2_prime.prime(5)"
# 1000 loops, best of 5: 19.2 usec per loop

# "task_2_prime.prime(10)"
# 1000 loops, best of 5: 163 usec per loop

# "task_2_prime.prime(20)"
# 1000 loops, best of 5: 1.33 msec per loop

# "task_2_prime.prime(50)"
# 1000 loops, best of 5: 25.4 msec per loop

# cProfile.run('prime(1)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_2_prime.py:9(prime)

# cProfile.run('prime(5)')
# 53 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_2_prime.py:9(prime)
# 9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 31    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 9    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}

# cProfile.run('prime(10)')
# 228 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_2_prime.py:9(prime)
# 27    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 170    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 27    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}

# cProfile.run('prime(20)')
# 942 function calls in 0.002 seconds
# 1    0.001    0.001    0.002    0.002 task_2_prime.py:9(prime)
# 69    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 800    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 69    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}

# cProfile.run('prime(50)')
# 6840 function calls in 0.027 seconds
# 1    0.027    0.027    0.027    0.027 task_2_prime.py:9(prime)
# 227    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 6382    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 227    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}

"""
Хотя при поиске первого простого числа алгоритм, не использующий 'Решето Эратосфена', показывает более быстрый 
результат, но при увеличении номера простого числа, которое мы хотим получить, алгоритм, использующий 'Решето 
Эратосфена', показывает значительный выигрыш по времени выполнения алгоритма.
"""
