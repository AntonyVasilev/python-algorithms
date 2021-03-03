"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, namedtuple


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class MyLeaf:

    def __init__(self, char):
        self.char = char

    def walk(self, code, acc):
        code[self.char] = acc or '0'


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_codding(string):
    assert len(string) > 0, 'Строка не может быть пустой'

    h = []
    for char, freq in Counter(s).items():
        # h.append((freq, len(h), Leaf(char)))
        h.append((freq, len(h), MyLeaf(char)))

    count = len(h)
    while len(h) > 1:
        freq_1, _count_1, left = h.pop(0)
        freq_2, _count_2, right = h.pop(0)
        # h.append((freq_1 + freq_2, count, Node(left, right)))
        h.append((freq_1 + freq_2, count, MyNode(left, right)))
        h.sort(key=lambda x: x[0])
        count += 1

    [(_freq, _count, root)] = h
    code = {}
    root.walk(code, '')
    return code


if __name__ == '__main__':
    s = input('Введите строку: ')

    code_dict = huffman_codding(s)
    encoded_string = "".join(code_dict[char] for char in s)
    print('Таблица кодов символов:')
    for ch in code_dict:
        print(f'{ch}: {code_dict[ch]}')

    print('*' * 80)
    print(f'Закодированная строка:\n{encoded_string}')
