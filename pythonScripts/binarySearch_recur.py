#!/usr/bin/python

#Binary search with recursion
def binary_search_recursive(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right ) // 2
    if array[middle] == target:
        return middle
    elif target < array[middle]:
        return binary_search_recursive(array, target, left, middle - 1)
    else:
        return binary_search_recursive(array, target, middle + 1, right)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
result = binary_search_recursive(array, target, 0, len(array) - 1)
print(result)

