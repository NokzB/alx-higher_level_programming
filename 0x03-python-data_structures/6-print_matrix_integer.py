#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        count = 0
        for val in matrix[i]:
            print("{:d}".format(val), end='')
            if count < len(matrix[i]) - 1:
                print(end=' ')
            count += 1
        print()
