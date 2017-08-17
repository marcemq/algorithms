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

    def inOrderTraversal(self, strTraversal=[]):
        """Traversal tree content inorder """
        if self.left:
            self.left.inOrderTraversal()
        strTraversal.append(str(self.data))
        if self.right:
            self.right.inOrderTraversal()
        return " ".join(strTraversal)

    def preOrderTraversal(self, strTraversal=[]):
        """Traversal tree content preorder """
        strTraversal.append(str(self.data))
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
        return " ".join(strTraversal)

    def postOrderTraversal(self, strTraversal=[]):
        """Traversal tree content postorder """
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        strTraversal.append(str(self.data))
        return " ".join(strTraversal)

    def getTreeHeight(self):
        """Return tree height """
        if not self.left and not self.right:
            return 0
        else:
            heightLeft = self.left.getTreeHeight() if self.left else 0
            heightRight = self.right.getTreeHeight() if self.right else 0
            return max(heightLeft, heightRight) + 1


if __name__ == "__main__":
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(4)
    print(root.inOrderTraversal())
    height = root.getTreeHeight()
    print("Tree height:{}".format(height))
