import sys

class Heap():
    """Heap class to manange minHeap and maxHeap.
    @typeHeapFlag: true refers a minHeap by default or maxHeap otherwise"""
    def __init__(self, typeHeapFlag=None):
        if typeHeapFlag == None:
            self.typeHeapFlag = True
        else:
            self.typeHeapFlag = typeHeapFlag
        self.items = []

    def __getLeftChildIndex(self, parentIndex): return 2*parentIndex + 1
    def __getRightChildIndex(self, parentIndex): return 2*parentIndex + 2
    def __getParentIndex(self, childIndex): return (childIndex - 1) // 2

    def __hasLeftChild(self, index):
        return self.__getLeftChildIndex(index) < len(self.items)
    def __hasRihtChild(self, index):
        return self.__getRightChildIndex(index) < len(self.items)
    def __hasParent(self, index):
        return self.__getParentIndex(index) >= 0

    def __getLeftChild(self, index):
        return self.items[self.__getLeftChildIndex(index)]
    def __getRightChild(self, index):
        return self.items[self.__getRightChildIndex(index)]
    def __getParent(self, index):
        return self.items[self.__getParentIndex(index)]

    def __swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def __outOfOrder(self, index):
        if self.typeHeapFlag:
            return self.__getParent(index) > self.items[index]
        else:
            return self.__getParent(index) < self.items[index]

    def __heapifyDownHelper(self, index):
        keyIndex = self.__getLeftChildIndex(index)
        if self.__hasRihtChild(index):
            rightChild = self.__getRightChild(index)
            leftChild = self.__getLeftChild(index)
            if self.typeHeapFlag and rightChild < leftChild:
                keyIndex = self.__getRightChildIndex(index)
            elif not self.typeHeapFlag and rightChild > leftChild:
                keyIndex = self.__getRightChildIndex(index)
        return keyIndex

    def __heapifyUp(self):
        index = len(self.items) - 1
        while self.__hasParent(index) and self.__outOfOrder(index):
            parentIndex = self.__getParentIndex(index)
            self.__swap(parentIndex, index)
            index = parentIndex

    def __heapifyDown(self):
        index = 0
        while self.__hasLeftChild(index):
            keyIndex = self.__heapifyDownHelper(index)
            if not self.__outOfOrder(keyIndex):
                break
            else:
                self.__swap(index, keyIndex)
            index = keyIndex

    def peek(self):
        if len(self.items) == 0:
            print("Heap is empty")
        else:
            return self.items[0]

    def poll(self):
        if len(self.items) == 0:
            print("Heap is empty")
        else:
            item = self.items[0]
            self.items[0] = self.items.pop()
            self.__heapifyDown()
            return item

    def add(self, item):
        self.items.append(item)
        self.__heapifyUp()

    def getType(self): return self.typeHeapFlag
    def getItems(self): return self.items
    def getLen(self): return len(items)

if __name__ == "__main__":
    data = [10, 15, 20, 17, 25]
    minHeap = Heap()
    maxHeap = Heap(typeHeapFlag=False)
    for i in range(len(data)):
        minHeap.add(data[i])
        maxHeap.add(data[i])

    print(minHeap.getItems())
    print(maxHeap.getItems())
    minHeap.poll()
    maxHeap.poll()
    print(minHeap.getItems())
    print(maxHeap.getItems())
