# If you were to perform a bubble sort on the following array, what would be the third iteration look like (i.e. after bubbling all the way up 3 times)?
# [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]


def bubbleSort(arr):
    arrLength = len(arr) - 1
    for index in range(arrLength):
        if arr[index] > arr[index + 1]:
            temp = arr[index]
            arr[index] = arr[index + 1]
            arr[index + 1] = temp
    return arr


def bubbleUp(n):
    arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    while n > 0:
        n -= 1
        print(bubbleSort(arr))


bubbleUp(3)
