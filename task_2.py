"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import shuffle


def merge(left_list, right_list):
    result_list = []
    list_index_l = 0
    list_index_r = 0

    list_l_len, list_r_len = len(left_list), len(right_list)

    for _ in range(list_l_len + list_r_len):
        if list_index_l < list_l_len and list_index_r < list_r_len:
            if left_list[list_index_l] <= right_list[list_index_r]:
                result_list.append(left_list[list_index_l])
                list_index_l += 1
            else:
                result_list.append(right_list[list_index_r])
                list_index_r += 1

        elif list_index_l == list_l_len:
            result_list.append(right_list[list_index_r])
            list_index_r += 1
        elif list_index_r == list_r_len:
            result_list.append(left_list[list_index_l])
            list_index_l += 1

    return result_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    avg_num = len(nums) // 2

    list_l = merge_sort(nums[:avg_num])
    list_r = merge_sort(nums[avg_num:])
    # print(list_l, list_r)

    return merge(list_l, list_r)


if __name__ == '__main__':
    array = [num for num in range(50)]
    shuffle(array)
    print(array)
    print('*' * 100)
    array = merge_sort(array)
    print(array)
