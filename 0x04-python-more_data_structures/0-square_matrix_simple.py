#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]

    return [list(map(lambda x: x ** 2, arr)) for arr in new_matrix]
