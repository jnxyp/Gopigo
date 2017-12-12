# coding=utf-8

from __future__ import print_function


def __process_two_lists_values(list1, list2, func):
    # type: (list, list, function) -> list
    if len(list1) < len(list2):
        list1 += [0] * (len(list2) - len(list1))
    elif len(list1) > len(list2):
        list2 += [0] * (len(list1) - len(list2))
    i = 0
    while i < len(list1):
        list1[i] = func(list1[i], list2[i])
        i += 1
    return list1


def add_two_lists_values(list1, list2):
    # type: (list, list) -> list
    # example:
    # >>> diff_two_lists_values([1,2,3,4],[-1,-2,-3])
    # [0,0,0,4]
    return __process_two_lists_values(list1, list2, lambda v1, v2: v1 + v2)


# print(add_two_lists_values([1, 2, 3, 4, 5], [-1, -2, -3]))

def diff_two_lists_values(list1, list2):
    # type: (list, list) -> list
    # example:
    # >>> diff_two_lists_values([1,2,3,4],[1,2,3])
    # [0,0,0,4]
    return __process_two_lists_values(list1, list2, lambda v1, v2: v1 - v2)



def __remove_stuff_at_end_of_list(list_in, func):
    # type: (list, function) -> list
    list_in = list_in[:]
    i = 0
    while i >= 0:
        if func(list_in[i]):
            list_in.pop()
        else:
            break
        i += 1
    return list_in

def remove_zeros_at_end_of_list(list_in):
    return __remove_stuff_at_end_of_list(list_in, lambda x: x == 0)


# print(remove_zeros_at_end_of_list([0,0,0,0,0,1,0,0,0,0,0]))
