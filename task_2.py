"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
# from binarytree import Node, build
from collections import Counter, OrderedDict, namedtuple
import heapq


# class MyNode:
#
#     def __init__(self, data, weight=0, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#         self.weight = weight


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_codding(string):
    assert len(string) > 0, 'Строка не может быть пустой'

    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq_1, _count_1, left = heapq.heappop(h)
        freq_2, _count_2, right = heapq.heappop(h)
        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))
        count += 1

    [(_freq, _count, root)] = h
    code_dict = {}
    root.walk(code_dict, '')
    return code_dict



if __name__ == '__main__':
    s = 'beep boop beer!'

    code = huffman_codding(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)


# s = input('Введите строку: ')
# print(huffman_codding(s))

# s = 'beep boop beer!'
#
# count_dict = Counter(s)

#
# print(count_dict)
#
# sorted_list = [[value, key] for key, value in count_dict.items()]
# sorted_list.sort()
#
# print(sorted_list)
#
#
# while len(sorted_list) > 1:
#     temp_list_1 = sorted_list.pop(0)
#     temp_list_2 = sorted_list.pop(0)
#     spam = [temp_list_1[0] + temp_list_2[0], [temp_list_1[1], temp_list_2[1]]]
#     sorted_list.append(spam)
#     sorted_list.sort(key=lambda x: x[0])
#     # spam = [temp_list_1[0] + temp_list_2[0], MyNode(None)]
#     # spam[1].left = MyNode(temp_list_1, weight=0)
#     # spam[1].right = MyNode(temp_list_2, weight=1)
#
#     # sorted_list.append(spam)
#     # sorted_list.sort(key=lambda x: x[0])
#
#     print(1)
#
# print(sorted_list)













# opposite_dict = {value: key for key, value in count_dict.items()}
# print(opposite_dict)
#
# chars_dict = OrderedDict(sorted(count_dict.items(), key=lambda x: x[1]))
# print(chars_dict)

