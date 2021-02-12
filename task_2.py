even_num = 0
odd_num = 0

num = input('Введите натуральное число: ')

for digit in num:
    if int(digit) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print(f'Количество четных чисел в числе {num} равно {even_num}, нечетных - {odd_num}.')
