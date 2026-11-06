#!/usr/bin/python3
def element_at(my_list, idx):
    last_Index = len(my_list)-1
    if (idx < 0 or idx > last_Index):
        return None
    else:
        return my_list[idx]
