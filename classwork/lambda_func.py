#!/usr/bin/python

# lambda arguments : expression
x = lambda a : a + 10
print(x(2))

add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
mod = lambda a, b : a % b
div = lambda a, b : a / b

def newFunc(y):
    return lambda a : a * y

i = newFunc(5)
print(i(2))

