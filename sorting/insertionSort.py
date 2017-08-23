import sys

def insertionSort(data):
    """ Implementation of the insertion sort algorithm in ascending order """
    for unsortedIndex in range(len(data)):
        unsortedData = data[unsortedIndex]
        sortedIndex = unsortedIndex
        while sortedIndex > 0 and unsortedData < data[sortedIndex-1]:
            data[sortedIndex] = data[sortedIndex-1]
            sortedIndex -= 1
        data[sortedIndex] = unsortedData
    return data

if __name__ == "__main__":
    data = [4, -31, 0, 99, 83, 1]
    print("Sorting {}".format(data))
    print("Sorted data:{}".format(insertionSort(data)))
