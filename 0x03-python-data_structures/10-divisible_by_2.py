#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = list(map(lambda i: bool(my_list[i] % 2 == 0),
                        range(len(my_list))))
    return new_list
