"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

result_dict = {i: [] for i in range(2, 10)}

for num in range(2, 100):
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

for i in range(2, 10):
    print(f'Числа, кратные {i}: {result_dict[i]}')
