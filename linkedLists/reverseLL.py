# Assume that you have a singly linked list,
# How would go about implementing a reverse funciton to it?
# Time Complexity? O(n) Why?
# N is the number of nodes in the linked list
# Loop runs once through each node in the list
# Space Complexity? O(1) Why?
# Algorithm uses fixed number of pointers and constant space.

def reverseLL(self):
    # prev will eventually become the new tail (None)
    # current starts at the head of the list
    prev = None
    current = self.head

    # We loop through the list until we've process all nodes
    while current:
        # Saves the next node so we don't lose it when changing pointers
        next_node = current.next
        # Reverses, or swaps, the link. Point the current node back to the previous node
        current.next = prev
        # Moves the previous and current 
        # forward to keep going through the list
        prev = current
        current = next_node

    # Updates head to the new front
    self.head = prev

# Assume that you have doubly linked list,
# How would you go about implementing a reverse function to it?
# Time Complexity?

def reverseDLL(self):
    # Starting from the head of the list
    # Temp is used to store pointers during swappin
    current = self.head
    temp = None

    while current:
        # Saves current.prev to temp
        temp = current.prev
        # Swap next and prev
        current.prev = current.next
        # Moves current.next to temp because we just swapped them
        current.next = temp

        # Move to the next node (previous now)
        current = current.prev

    # Update head to the last non-null node
    # After the loop, temp holds the second-to-last node we visited
    # temp.prev is the new head of the list
    if temp:
        self.head = temp.prev