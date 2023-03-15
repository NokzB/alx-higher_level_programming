#!/usr/bin/python3
def max_integer(my_list=[]):
    for x in my_list:
        if x == 0:
            return None
        else:
            my_list.sort()
            print('{:d}', my_list[-1])
