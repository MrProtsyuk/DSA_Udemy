# Implement a queue using stacks problem
# Goal is to simulate FIFO behaviour using LIFO

class QueueUsingStacks:
    def __init__(self):
        # Two empty lists
        # StackIN => handles enqueue operations, i.e all new data incoming
        # StackOUT => handles dequeue and peek, i.e all out going data 
        self.stackIn = []
        self.stackOut = []

    # Checks if the "Queue" is empty or not
    def empty(self):
        return not self.stackIn and not self.stackOut

    # appends the data to stackIn, why use stackIn? 
    # because we are maintaining the reversed queue order
    # until we need to dequeue or peek 
    def enqueue(self, data):
        self.stackIn.append(data)

    # if stack out is empty, we need to reverse the order
    # of stackIn into stackOut. Makes the first item enqueue become the 
    # top of stackOut. 
    def dequeue(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        # If stackOut is still empty, we just raise an error
        if not self.stackOut:
            raise IndexError("Queue is empty")
        # Else, we pop the top of stackOut which is the front of the queue
        return self.stackOut.pop()

    # Same idea as dequeue, moving in reverse order to move items from stackIn
    # into stackOut
    def peek(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        # If stackOut is still empty, we just raise an error
        if not self.stackOut:
            raise IndexError("Queue is empty")
        # Else, we return the last item in stackOut (list) which would be the first item in the queue.
        return self.stackOut[-1]