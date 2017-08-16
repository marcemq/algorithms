import sys

class Node():
    """
    Tree node: holds a left and right childs along with data
    """
    def __init__(self, data=None):
        """Node constructor """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """Insert new node with data """
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def inOrderTraversal(self):
        """Traversal tree content inorder """
        if self.left:
            self.left.inOrderTraversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        """Traversal tree content preorder """
        print(self.data, end=" ")
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    def postOrderTraversal(self):
        """Traversal tree content postorder """
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.data, end=" ")


if __name__ == "__main__":
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.inOrderTraversal(), print()
    root.preOrderTraversal(), print()
    root.postOrderTraversal(), print()
