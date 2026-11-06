#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last_Index = len(my_list) - 1
    print(my_list[last_Index])
    while True:
        last_Index = last_Index - 1
        if (last_Index < 0):
            break
        print(my_list[last_Index])
