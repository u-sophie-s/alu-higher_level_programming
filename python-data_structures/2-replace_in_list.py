#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    last_Index = len(my_list) - 1
    if(idx < 0 or idx > last_Index ):
        return my_list
    else:
        my_list[idx] = element
        return my_list
