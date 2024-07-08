#!/usr/bin/python

def searchString(strList, searchString):
    s = 0
    e = len(strList) - 1
    totalSearchString = 0
    for i in searchString:
        totalSearchString += ord(i)
    while s <= e:
        m = s + e // 2
        totalStart = 0
        totalMiddle = 0
        for i in s:
            total
