#!/usr/bin/python


def factorialWithLoop(x):
    sum = 1
    i = 1
    while i <= x:
        sum *= i
        i += 1
    return sum

def factorial(x):
    if x == 1:
        return 1
    return(x * factorial(x - 1))

print(factorial(5))

