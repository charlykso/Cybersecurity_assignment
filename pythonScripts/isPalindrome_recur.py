#!/usr/bin/python

#Checking if a word is a palindrome with recursion
def is_palindrome_recursively(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome_recursively(s[1:-1])
    return False

s = "tundednute"
print(is_palindrome_recursively(s))

