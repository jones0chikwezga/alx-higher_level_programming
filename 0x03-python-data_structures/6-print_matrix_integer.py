#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            if item == row[len(row) - 1]:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
        print()
