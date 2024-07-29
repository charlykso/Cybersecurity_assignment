#!/usr/bin/python

import sys

def div(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("This is another exception")
        return a / b
    except ZeroDivisionError:
        return "An exception occurs"

def main():
    argv = sys.argv
    if len(argv) != 3:
        print("Error: usage ./filename num1 num2")
        return -1
    print(div(int(argv[1]), int(argv[2])))
    return 0

if __name__ == "__main__":
    main()

