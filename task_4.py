"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

from string import ascii_lowercase

letters = ascii_lowercase

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

a = a.lower()
b = b.lower()
a_pos = letters.find(a)
b_pos = letters.find(b)
print(f'Буква {a} находится на {a_pos + 1} месте в алфавите.')
print(f'Буква {b} находится на {b_pos + 1} месте в алфавите.')

if a_pos > b_pos:
    print(f'Между буквами {a} и {b} находится {a_pos - b_pos} букв.')
else:
    print(f'Между буквами {a} и {b} находится {b_pos - a_pos} букв.')
