#!/usr/bin/python

def findSum(arr, k):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == k:
                return [i, j]
            j += 1
        i += 1
    return -1

x = [1, 3, 4, 5, 9, 10, 14, 16]
print(findSum(x, 9))

