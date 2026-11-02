#!/usr/bin/python3
def fizzbuzz():
    for num in range(100):
        if (num%3 == 0):
            print("Fizz")
        elif (num%5 == 0):
            print("Buzz")
        elif (num%3 & num%5):
            print("FizzBuzz")
        else:
            print(num)
fizzbuzz()
