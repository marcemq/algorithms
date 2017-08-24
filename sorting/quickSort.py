import sys

def quickSort(data, leftIndex, rightIndex):
    """ Implementation of the merge sort algorithm in ascending order """
    if len(data) > 1:
        pivotIndex = partition(data, leftIndex, rightIndex)
        if leftIndex < pivotIndex-1:
            quickSort(data, leftIndex, pivotIndex-1)
        if  pivotIndex < rightIndex:
            quickSort(data, pivotIndex, rightIndex)
    return data

def partition(data, left, right):
    """ Partition data around a middle-most element """
    pivot = data[(int)((left+right)/2)]
    while left <= right:
        if data[left] > pivot and data[right] < pivot:
            data[left], data[right] = data[right], data[left]
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1
    # The left index becomes the new pivot index
    return left

if __name__ == "__main__":
    data = [19, 22, 63, 105, 2, 46]
    print("Sorting {}".format(data))
    print("Sorted data:{}".format(quickSort(data, 0, len(data)-1)))
