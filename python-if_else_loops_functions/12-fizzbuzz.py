#!/usr/bin/python3
def fizzbuzz():
    for num in range(100):
        if (num%3 == 0):
            print("Fizz", end=" ")
        elif (num%5 == 0):
            print("Buzz", end=" ")
        elif (num%3 & num%5):
            print("FizzBuzz", end=" ")
        else:
            print(num, end=" ")
fizzbuzz()
