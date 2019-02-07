"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    mid = []
    lesser = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for num in array:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                lesser.append(num)
        return quicksort(lesser) + mid + quicksort(greater)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
