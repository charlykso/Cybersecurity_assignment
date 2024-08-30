#!/usr/bin/python

def binSearch(arr, k):
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = s + e // 2
        if arr[m] == k:
            return m
        if arr[m] > k:
            e = m - 1
        if arr[m] < k:
            s = m + 1
    return -1

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(binSearch(x, 20))

