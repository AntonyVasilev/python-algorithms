"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from binarytree import Node, build
from collections import Counter


def huffman_codding(string):
    assert len(string) > 0, 'Строка не может быть пустой'
    pass


# s = input('Введите строку: ')
# print(huffman_codding(s))

s = 'beep boop beer!'

count_dict = Counter(s)
print(count_dict)
chars_list = []

# for char in count_dict.keys():
#     chars_list.append(char)

print(list(chars_list))



