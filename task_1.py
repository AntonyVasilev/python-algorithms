"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
задача считается не решённой.
"""

import hashlib


def substrings_count(string):
    assert len(string) > 0, 'Строка не может быть пустой'
    if len(string) == 1:
        return 1

    str_length = len(string)
    substrings = set()

    for i in range(1, str_length):
        for j in range(str_length + 1 - i):
            spam = hashlib.sha1(string[j: j + i].encode('utf-8')).hexdigest()
            substrings.add(spam)

    return len(substrings) - 1


s = input('Введите строку: ')
print(f'Количество подстрок: {substrings_count(s)}')



