#!/usr/bin/python3

def max_integer(my_list=[]):
    if (not my_list):
        return None

    max_num = my_list[0]

    for i in range(len(my_list)):
        if (max_num > my_list[i]):
            continue
        max_num = my_list[i]

    return max_num
