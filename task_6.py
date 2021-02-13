"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""

from random import randint

n = randint(0, 100)
i = 10

while True:
    i -= 1
    answer = int(input('Введите число: '))

    if answer == n:
        print('Вы угадали!')
        break
    elif answer > n:
        print(f'Введенное число больше загаданного. У вас осталось {i} попыток.')
    else:
        print(f'Введенное число меньше загаданного. У вас осталось {i} попыток.')

    if i == 0:
        print(f'Вы не угадали. Правильный ответ {n}.')
        break
