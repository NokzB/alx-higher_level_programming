#!/usr/bin/python3
"""
Backtracking nqueens program that prints coordinates of n queens
on an nxn grid in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initializes the answer list
    for i in range(n):
        a.append([i, None])

    def check_exists(y):
        """checks that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def rejects(x, y):
        """determines whether to reject the solution or not"""
        if (check_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_answers(x):
        """clears all the answers from the point of failure"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """backtracking function to find solution"""
        for y in range(n):
            clear_answers(x)
            if rejects(x, y):
                a[x][1] = y
                # accepts the solution
                if (x == n - 1):
                    print(a)
                else:
                    # moves onto the next x value
                    nqueens(x + 1)

    # starts the process at position x = 0
    nqueens(0)
