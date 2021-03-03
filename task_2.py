"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, path):
        self.left.walk(code, path + '0')
        self.right.walk(code, path + '1')


class MyLeaf:

    def __init__(self, char):
        self.char = char

    def walk(self, code, path):
        code[self.char] = path or '0'


def huffman_codding(string):
    assert len(string) > 0, 'Строка не может быть пустой'

    chars_list = []
    for char, freq in Counter(string).items():
        chars_list.append((freq, MyLeaf(char)))
    chars_list.sort(key=lambda x: x[0])

    while len(chars_list) > 1:
        freq_1, left = chars_list.pop(0)
        freq_2, right = chars_list.pop(0)
        chars_list.append((freq_1 + freq_2, MyNode(left, right)))
        chars_list.sort(key=lambda x: x[0])

    [(_freq, tree)] = chars_list
    code = {}
    tree.walk(code, '')
    return code


if __name__ == '__main__':
    s = input('Введите строку: ')

    code_dict = huffman_codding(s)
    encoded_string = ' '.join(code_dict[char] for char in s)
    print('Таблица кодов символов:')
    for ch in code_dict:
        print(f'{ch}: {code_dict[ch]}')

    print('*' * 40)
    print(f'Закодированная строка:\n{encoded_string}')
