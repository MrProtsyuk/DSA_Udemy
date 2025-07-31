from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a key into the BST
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    # Search for a key in the BST
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # In-order traversal (left-root-right)
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            return []
        return self._inorder(root.left) + [root.key] + self._inorder(root.right)

    def breadthFirstSearch(self):
        result = []
        if not self.root:
            return result

        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.key)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        return result

tree = BinarySearchTree()
tree.insert(9)
tree.insert(20)
tree.insert(5)
tree.insert(2)
tree.insert(81)
tree.insert(80)
print(tree.inorder())
print(tree.breadthFirstSearch())