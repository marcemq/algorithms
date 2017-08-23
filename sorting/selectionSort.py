import sys

def selection(data):
    """ Implementation of the selection sort algorithm """
    n = len(data)
    for index in range(n):
        minDataIndex = index
        for nextDataIndex in range(index+1, n):
            if data[minDataIndex] > data[nextDataIndex]:
                minDataIndex = nextDataIndex
        if minDataIndex != index:
            data[index], data[minDataIndex] = data[minDataIndex], data[index]
    return data

if __name__ == "__main__":
    data = [33,2,52,106,73]
    print("Sorting {}".format(data))
    print("Sorted data:{}".format(selection(data)))
