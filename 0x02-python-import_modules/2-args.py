#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    counter = len(argv) - 1
    if counter < 1:
        print("{:d} arguments.".format(counter))
    elif counter == 1:
        print("{:d} argument:".format(counter))
    else:
        print("{:d} arguments:".format(counter))
for i in range(counter):
    print("{:d}: {:s}".format(i + 1, argv[i + 1]))
