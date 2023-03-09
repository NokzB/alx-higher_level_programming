#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    counter = len(argv) - 1
    if counter < 1:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
for i in range(counter):
    print("{}: {}".format(i + 1, argv[i + 1]))
