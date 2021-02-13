"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

max_num = 0
max_sum = 0

num_amount = int(input('Введите количество чисел: '))

for i in range(num_amount):
    digits_sum = 0
    user_num = input(f'Введите {i + 1} число: ')
    for digit in user_num:
        digits_sum += int(digit)

    if digits_sum > max_sum:
        max_sum = digits_sum
        max_num = int(user_num)

print(f'Максимальное число по сумме его цифр - {max_num}, сумма его цифр - {max_sum}.')
