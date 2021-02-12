opposite_num = ''

num = input('Введите число: ')

for digit in num:
    opposite_num = f'{digit}{opposite_num}'

print(f'Обратное {num} число: {opposite_num}')
