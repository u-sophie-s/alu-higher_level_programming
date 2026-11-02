#!/usr/bin/python3
def islower(str):
    for char in str:
        if (str == ""):
            return "error"
        else:
            if ord(char) >= 97 and ord(char) <= 122:
               return True
            else:
               return False
