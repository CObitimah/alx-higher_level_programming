#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for num in row:

            print ("{:d}".format(num), end=" ")
            print()
