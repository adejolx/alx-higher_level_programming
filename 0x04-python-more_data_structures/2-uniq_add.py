#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    uniq_list = list(new_set)
    sum = 0

    for i in range(len(uniq_list)):
        sum += uniq_list[i]

    return sum
