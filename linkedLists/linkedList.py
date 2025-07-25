# Node class, each node represents a single element
class Node:
    def __init__(self, data):
        # This value is store in the node
        self.data = data
        # This is the reference to the next node.
        # Initializing a pointer to the next node
        self.next = None
        # This is the reference to the previous node.
        # Initializing a pointer to the previous node
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Adds a node to the end of the list
        new_node = Node(data)
        # If the list is empty, then the new node
        # becomes the head of the list
        if self.head is None:
            self.head = new_node
            return
        # start at the head of the list
        current = self.head
        # Moves through the list until reaching the last node
        while current.next:
            current = current.next
        # when current.next = None, it is set to the new node
        current.next = new_node
        # Link back to the previous node
        new_node.prev = current

    def prepend(self, data):
        # Adds a node to the beginning of the list
        new_node = Node(data)
        # points to the new node .next to the current head
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        # sets the new node to be the head
        self.head = new_node

    def delete(self, key):
        # Deletes the first node with the given data
        current = self.head

        # If the node that is to be deleted is the head
        # Set the head to the next node
        if current and current.data == key:
            self.head = current.next
            return
        
        # Traverse the list until finding the node with
        # matching data, keeps track of previous node.
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            # If key not found
            return
        
        # remove the node by making the previous node skip over it
        prev.next = current.next

    def insert(self, index, data):
        # Insert a node with data at the index
        new_node = Node(data)

        # Negative Index error check
        if index < 0:
            raise IndexError("Index must be non-negative")
        
        # Insert at the head if index is zero
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # starts the traversal at the head of the list
        current = self.head
        current_index = 0

        # Traverse to the node just before the desired index
        # If current become None before that, it means the index is out of bounds
        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("Index out of bounds")
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        # Remove the first node that contains the given data
        current = self.head
        
        # Traverse the list to find the node
        while current and current.data != data:
            current = current.next

        # If data not found
        if not current:
            return
        
        # Udate the previous node
        if current.prev:
            current.prev.next = current.next
        else:
            # Removes the head
            self.head = current.next 
        
        # Update the next node
        if current.next:
            current.next.prev = current.prev

    # Specifically done with Singly Linked List functionality in mind
    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Saves the next node; 
            next_node = current.next
            # Reverses, or swaps, the link; 
            current.next = prev
            # Moves the previous forward
            prev = current
            # Moves current forward
            current = next_node

        # Updates head to the new fron
        self.head = prev

    def print_forward(self):
        # Prints all elements in the list
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.head
        while current and current.next:
            # Moves to tail
            current = current.next 

        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")

ll = DoublyLinkedList()
ll.append(10)
ll.append(20)
ll.print_forward()
ll.prepend(5)
ll.print_forward()
ll.insert(2, 99)
ll.print_forward()
ll.delete(10)
ll.print_forward()
ll.reverse()
ll.print_forward()