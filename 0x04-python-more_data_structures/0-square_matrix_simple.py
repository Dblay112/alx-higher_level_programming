#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_line = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_line.append(new_row)

    return new_line

