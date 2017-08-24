import sys

def mergeSort(data):
    """ Implementation of the merge sort algorithm in ascending order """
    n =  len(data)
    if n == 1:
        return data
    else:
        midIndex = (int)(n/2)
        leftHalf = mergeSort(data[0:midIndex])
        rightHalf = mergeSort(data[midIndex:n])
        return mergeHalves(leftHalf, rightHalf)

def mergeHalves(leftHalf, rightHalf):
    """ Merge two halves and return the merged data list """
    sortedData = list()
    while leftHalf and rightHalf:
        smallerDataHolder = leftHalf if leftHalf[0] < rightHalf[0] else rightHalf
        minData = smallerDataHolder.pop(0)
        sortedData.append(minData)
    remaininData = leftHalf if leftHalf else rightHalf
    while remaininData:
        sortedData.append(remaininData.pop(0))
    return sortedData

if __name__ == "__main__":
    data = [5, 1, 7, 3, 2, 8, 6, 4]
    print("Sorting {}".format(data))
    print("Sorted data:{}".format(mergeSort(data)))
