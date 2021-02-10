"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

from string import ascii_lowercase

letters = ascii_lowercase
a = input('Введите букву: ')
print(f'Буква {a} - {letters.find(a) + 1}-я буква в алфавите.')
