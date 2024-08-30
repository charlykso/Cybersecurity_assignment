#!/usr/bin/python

#String reversal with recursion
def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

s = "hello"
print(reverse_string_recursive(s))

