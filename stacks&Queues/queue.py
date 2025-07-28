# Implementing Queue class using Linked Lists

# Node class to keep track of links
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Keeping track of first and last and length
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        # Prints all elements in the list
        current = self.first
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Simple method to look at the first node
    def peek(self):
        if self.first == None:
            return self.__str__()
        
        return print(self.first.data)

    # Simple method to add nodes to the list
    def enqueue(self, data):
        new_node = Node(data)

        # If the first node is None, set it to the new node
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self.__str__()
    
        # Else, add the new node to the end 
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return self.__str__()
    
    # Simple dequeue method to check for empty list and to remove first item
    def dequeue(self):
        if self.first is None:
            return self.__str__()
        
        if self.first == self.last:
            self.last = None

        # Moving whatever was after the first node into the first node
        self.first = self.first.next
        self.length -= 1
        return self.__str__()

myQueue = Queue()
myQueue.enqueue("Mark")
myQueue.enqueue("Bob")
myQueue.dequeue()
myQueue.dequeue()