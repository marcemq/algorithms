import sys
sys.path.insert(0, "../dataStructures")

from heap import Heap

def addNumber(number, lowers, highers):
    """ Add a number into the heaps. """
    if lowers.getLen() == 0 or number < lowers.peek():
        lowers.add(number)
    else:
        highers.add(number)

def rebalance(lowers, highers):
    """ Rebalance heaps so its sizes differ in no more than one item. """
    biggerHeap = lowers if lowers.getLen() > highers.getLen() else highers
    smallerHeap = highers if lowers.getLen() > highers.getLen() else lowers
    if (biggerHeap.getLen() - smallerHeap.getLen()) > 1:
        smallerHeap.add(biggerHeap.poll())

def getMedian(lowers, highers):
    """ Return median from current content on heaps. """
    biggerHeap = lowers if lowers.getLen() > highers.getLen() else highers
    smallerHeap = highers if lowers.getLen() > highers.getLen() else lowers
    if biggerHeap.getLen() == smallerHeap.getLen():
        return (lowers.peek() + highers.peek()) / 2.0
    else:
        return biggerHeap.peek()

def getMedians(a):
    """ Return medians array. """
    medians = list()
    highers = Heap()
    lowers = Heap(typeHeapFlag=False)
    for i in range(len(a)):
        addNumber(a[i], lowers, highers)
        rebalance(lowers, highers)
        medians.append(getMedian(lowers, highers))
    return medians

if __name__ == "__main__":
    data = [12, 4, 5, 3, 8, 7]
    medians = getMedians(data)
    print(*medians, sep="\n")
