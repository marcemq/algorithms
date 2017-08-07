import sys

class Node():
    """ Simple node class."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList():
    """ Linked list class."""
    def __init__(self, head=None):
        self.head = head

    def __traverseNthFromHead(self, n):
        count = 0
        nodeit = self.head
        while nodeit.next != None and count < n:
            nodeit = nodeit.next
            count += 1
        return nodeit

    def __traverseToEnd(self):
        nodeit = self.head
        while nodeit.next != None:
            nodeit = nodeit.next
        return nodeit

    def insertFirst(self, data):
        self.insertNth(data, 0)

    def insertLast(self, data):
        self.insertNth(data)

    def insertNth(self, data, n=None):
        if self.head:
            node = Node(data)
            if n == 0:
                node.next, self.head = self.head, node
            else:
                count = 0
                nodeit = self.__traverseNthFromHead(n-1) if n!=None else self.__traverseToEnd()
                node.next, nodeit.next = nodeit.next, node
        else:
            self.head = Node(data)

    def deleteNth(self, n):
        if self.head:
            if n == 0:
                self.head  = self.head.next
            else:
                count = 0
                nodeit = self.__traverseNthFromHead(n-1)
                nodeit.next = nodeit.next.next
        else:
            print("Linked List is empty")

    def printList(self):
        node = self.head
        while node != None:
            print("{}".format(node.data), end=" ")
            node = node.next
        print()

if __name__ == "__main__":
    x = LinkedList()
    y = LinkedList()
    data = [5, 3, 7, 1, 25]
    for i in range(len(data)):
        x.insertFirst(data[i])
        y.insertLast(data[i])
    x.printList()
    y.printList()
    x.insertNth(-1, 3)
    x.printList()
    x.deleteNth(5)
    x.printList()
