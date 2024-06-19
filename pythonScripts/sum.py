#!/usr/bin/python

import random

#printing a random number
print(random.randrange(1, 10))

#declaring a variable
num1 = 10.5
num2 = 6
num3 = int(num1)
num4 = float(num2)
num5 = str(num1)

print(f"{num1} was converted from {type(num1)} to {num3} of type {type(num3)} and {num2} converted from {type(num2)} to {num4} of type {type(num4)}")
print(f"{num1} was converted from {type(num1)} to {num5} of type {type(num5)}")

