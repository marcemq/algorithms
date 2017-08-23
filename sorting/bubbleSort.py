import sys

def bubbleSort(data):
    """ Implementation of the bubble sort algorithm in ascending order """
    isSorted = False
    n = len(data)
    lastInOrder = 0
    while not isSorted:
        isSorted = True
        for index in range(1, n - lastInOrder):
            if data[index-1] > data[index]:
                isSorted = False
                data[index-1], data[index] = data[index], data[index-1]
        lastInOrder += 1
    return data

if __name__ == "__main__":
    data = [9, 7, 4, 1, 2]
    print("Sorting {}".format(data))
    print("Sorted data:{}".format(bubbleSort(data)))
