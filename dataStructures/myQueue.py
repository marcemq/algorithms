# Problem taken from hackerrank
# Queues: A Tale of Two Stacks
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
#
# In this challenge, you must first implement a queue using two stacks.
# Then process q  queries, where each query is one of the following  types:
# 1 x: Enqueue element x into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.

import sys

class MyQueue():
    """MyQueue class to manange a standar queue using two stacks """
    def __init__(self):
        self.stackNewestOnTop = list()
        self.stackOldestOnTop = list()

    def enqueue(self, item):
        """ Add item into queue"""
        self.stackNewestOnTop.append(item)

    def dequeue(self):
        """ Get oldest item and remove it from queue. """
        self.__shiftStacks()
        if self.stackOldestOnTop:
            return self.stackOldestOnTop.pop()
        else:
            print("There is not items on queue.")

    def peek(self):
        """ Get oldest item from queue. """
        self.__shiftStacks()
        if self.stackOldestOnTop:
            return self.stackOldestOnTop[len(self.stackOldestOnTop) - 1]
        else:
            print("There is not items on queue.")

    def __shiftStacks(self):
        if not self.stackOldestOnTop:
            while self.stackNewestOnTop:
                self.stackOldestOnTop.append(self.stackNewestOnTop.pop())

if __name__ == "__main__":
    queue = MyQueue()
    values = [[1, 76], [1, 33], [2], [1, 23], [1, 97], [1, 21], [3], [3], [1, 74], [3]]
    for i in range(len(values)):
        if values[i][0] == 1:
            queue.enqueue(values[i][1])
        elif values[i][0] == 2:
            queue.dequeue()
        elif values[i][0] == 3:
            print(queue.peek())
