#!/usr/bin/python3
"""Backtracking Program to print the coordinates of n queens
on an nxn grid in non_attacking positions
"""

import sys

if __name__ == "__main__":
    a = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N Must be at least 4")
        exit(1)

    # initializes the answer list
    for i in range(n):
        a.append([i, None])

    def exists(y):
        """Checks if the queen does not already exists in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject_sol(x, y):
        """determines whether to accept or reject the solution"""
        if (exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
            return True

    def clear_answer(x):
        """clears the answers from where it fails"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """backtracking function to find solution"""
        for y in range(n):
            clear_answer(x)
            if reject_sol(x, y):
                a[x][1] = y
                # accepts solution
                if (x == n - 1):
                    print(a)
                else:
                    # moves onto the next x value to continue
                    nqueens(x + 1)

    # starts the process at x = 0
    nqueens(0)
