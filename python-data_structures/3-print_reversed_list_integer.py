#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return

    last_index = len(my_list) - 1
    print("{:d}".format(my_list[last_index]))

    while True:
        last_index -= 1
        if last_index < 0:
            break
        print("{:d}".format(my_list[last_index]))
