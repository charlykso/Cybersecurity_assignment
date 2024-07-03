#!/usr/bin/python

import sys

def main():
    argv = sys.argv
    if len(argv) != 4:
        print("Error: usage ./filename x y z")
        return -1
    x = argv[1]
    y = argv[2]
    z = argv[3]
    largest = z
    if x > largest:
        largest = x
    elif y > largest:
        largest = y
    print(f"The largest number is {largest}")



if __name__ == "__main__":
    main()

