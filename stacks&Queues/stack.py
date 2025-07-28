# Implementation of a Stack with Linked Lists
# Node class to keep track of links
class Node:
    def __init__(self, data):
        self.data = data
        # Since it is a stack we only need to go to the next one
        self.next = None

# Stack Linked List Class
class StackLL:
    def __init__(self):
        # Keeping track of top and bottom and length
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        # Prints all elements in the list
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Simple peek at the top item of the stack
    def peek(self):
        # Return None if nothing at the top
        if self.top is None:
            return None
        return print(self.top.data)
    
    # Simple Push to the stack
    def push(self, data):
        # Creating a new node from the data passed in
        new_node = Node(data)

        # If nothing in stack, new node equals top
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
            self.length += 1
            return self.__str__()
        
        # Else, push top to the next and make new node the top
        current = self.top
        self.top = new_node
        self.top.next = current
        self.length += 1

        return self.__str__()
    
    # Simple pop method for removing top node
    def pop(self):
        # If nothing in stack return none
        if self.top is None:
            return print(self.top)
        
        # If only one item in stack, set bottom to none to not double on count
        if self.top == self.bottom:
            self.bottom = None
        
        # Else, move current top to empty variable
        # Set top to whatever was after it
        current = self.top
        self.top = self.top.next
        self.length -= 1

        return self.__str__()

    
# myLLStack = StackLL()
# myLLStack.push(13)
# myLLStack.push(10)
# myLLStack.push(5)
# myLLStack.pop()
# myLLStack.pop()

# Implementing Stack class using arrays, a very simplified
# version of the class above because it uses python integrated
# array methods
class StackArr:
    def __init__(self):
        self.data = []

    def __str__(self):
        return print(self.data)

    def peek(self):
        if len(self.data) == 0:
            return self.data    
        return self.data[-1]

    def push(self, data):
        self.data.append(data)
        return self.__str__()
        
    def pop(self):
        if len(self.data) == 0:
            return self.data
        self.data.pop()
        return self.__str__()
    
myArrStack = StackArr()
myArrStack.push(13)
myArrStack.push(1)
myArrStack.push("Hello there again")
myArrStack.pop()
myArrStack.pop()
myArrStack.pop()
