"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

from string import ascii_lowercase

letters = ascii_lowercase
a = int(input('Введите номер буквы: '))
print(f'{a}-я буква в алфавите - {letters[a - 1]}.')
