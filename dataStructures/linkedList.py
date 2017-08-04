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

    def insertFirst(self, data):
        if self.head:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            self.head = Node(data)

    def insertLast(self, data):
        if self.head:
            node = Node(data)
            nodeit = self.head
            while nodeit.next != None:
                nodeit = nodeit.next
            nodeit.next = node
        else:
            self.head = Node(data)

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
