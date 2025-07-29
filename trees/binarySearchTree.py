# Implementing a binary search tree using a similar structure as Linked Lists

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        def traverse(node):
            if node is None:
                return []
            return traverse(node.left) + [node.data] + traverse(node.right)

        return print(str(traverse(self.root)))

    def insert(self, data):
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
            return self.__str__()
        
        current = self.root
        while current:
            # Go left
            if data < current.data:
                if current.left == None:
                    current.left = new_node
                    return self.__str__()
                current = current.left
            if data > current.data:
                if current.right == None:
                    current.right = new_node
                    return self.__str__()
                current = current.right

    def lookup(self, data):
        if self.root == None:
            return print("Tree is empty")
        current = self.root
        level = 0
        while current:
            if data < current.data:
                level += 1
                current = current.left
            elif data > current.data:
                level += 1
                current = current.right
            elif current.data == data:
                return print(f"Item {data} is on level {level}")
            
        return print("Item not found")

    def remove(self, data):
        if self.root == None:
            return print("Tree is empty")
        current = self.root
        parent = None
        while current:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current.right
            elif current.data == data:
                # No right child
                if current.right == None:
                    if parent == None:
                        self.root = current.left
                    else:
                        if current.data < parent.data:
                            parent.left = current.left
                        elif current.data > parent.data:
                            parent.right = current.left
                    return self.__str__()
                # Right child doesnt have a left child
                elif current.right.left == None:
                    if parent == None:
                        self.root = current.right
                    else:
                        current.right.left = current.left
                        if current.data < parent.data:
                            parent.left = current.left
                        elif current.data > parent.data:
                            parent.right = current.left
                    return self.__str__()
                # Right Child that has a left child
                # Imma be honest, I have no clue whats going on here, got pretty lost in the lesson
                else:
                    leftMost = current.right.left
                    leftMostParent = current.right
                    while leftMost.left != None:
                        leftMostParent = leftMost
                        leftMost = leftMost.left

                    leftMostParent.left = leftMost.right
                    leftMost.left = current.left
                    leftMost.right = current.right

                    if parent == None:
                        self.root = leftMost
                    else:
                        if current.data < parent.data:
                            parent.left = leftMost
                        elif current.data > parent.data:
                            parent.right = leftMost

            return self.__str__()
                



myBST = BinarySearchTree()
myBST.insert(2)
myBST.insert(5)
myBST.insert(3)
myBST.lookup(2)
# remove functionality does not work :/
myBST.remove(5)


