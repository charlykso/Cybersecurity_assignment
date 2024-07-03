#!/usr/bin/python

x = "Hello, World"
#[print(i) for i in x]
y = len(x) - 1
while y >= 0:
    print(x[y])
    y -= 1

def myFunction():
    print("My first function")

def myFunction(str):
    return str

def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def exp(a, b):
    return a ** b

def solve(a, b):
    return mult(mult(div(a, b), div(b, a)), a)

print(solve(2, 3))

