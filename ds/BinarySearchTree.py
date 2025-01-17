class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value < root.data:
            if not root.left:
                root.left = TreeNode(value)
            else:
                self._insert(root.left, value)
        else:
            if not root.right:
                root.right = TreeNode(value)
            else:
                self._insert(root.right, value)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, root, value):
        if root is None:
            return None
        elif value == root.data:
            return value
        elif value < root.data:
            return self._find(root.left, value)
        else:
            return self._find(root.right, value)


if __name__ == '__main__':
    # Example usage:
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    print(bst.find(1))
    print(bst.find(2))