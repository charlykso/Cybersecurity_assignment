#!/usr/bin/python
import sys

arguments = sys.argv

def sub(arguments):
    if len(arguments) <= 1:
        print("No argument provided")
        return 0
    elif len(arguments) == 3:
        a = arguments[1]
        b = arguments[2]
        return int(a) - int(b)
    else:
        print("Invalid input")
        return 0
if len(arguments) == 3:
    print("When you subtract {} from {} you will have {}".format(arguments[2], arguments[1], sub(arguments)))
else:
    sub(arguments)

