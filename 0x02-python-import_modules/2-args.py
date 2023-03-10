#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg <= 1:
        print("0 arguments.")
    else:
        if arg == 2:
            print("{:d} argument:".format(arg - 1))
        else:
            print("{:d} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{:d}: {}".format(i, sys.argv[i]))
