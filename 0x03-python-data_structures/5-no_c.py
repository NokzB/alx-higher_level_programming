#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord('c'): None})
    new_string2 = my_string.translate({ord('C'): None})
    print(new_string)
    print(new_string2)
