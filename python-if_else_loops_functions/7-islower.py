#!/usr/bin/python3
def islower(str):
    if not str:
        raise ValueError
    else:
        for char in str: 
            if ord(char) >= 97 and ord(char) <= 122:
                continue
            else:
                return False
    return True
