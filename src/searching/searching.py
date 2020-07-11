# searching through an already sorted list
def linear_search(arr, target):
    # Your code here
    # evaluate each element from the beginning until a match is found
    for i, e in enumerate(arr):
        if e == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # divide then conquer
    # Your code here
    if len(arr) == 0:  # empty arr
        return -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        current = arr[middle]
        if current < target:
            start = middle + 1
        elif current > target:
            end = middle - 1
        else:  # current = target
            return middle
    return -1  # not found
