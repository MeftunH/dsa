from py.BST.Node import Node


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def search(self, data):
        return self._search(self.root, data)

