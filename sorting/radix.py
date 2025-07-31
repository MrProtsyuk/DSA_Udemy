# Implementation of Radix sort
# Radix sort is non-comparative, meaning it sorts numbers by processing 
# individual digits (or groups of bits) from least significant to most 
# significant (LSD Radix Sort) or vice versa (MSD Radix Sort)
# Radix sort uses counting sort as a stable sorting algorithm

# Use case is only for integers, or anything that can be broken down to digits
# Time complexity: O(k * n) Why?
# K is the number of digits and n is the number of elements

# Counting sort function
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the current place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array, will be backwards
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output array back to original 
    for i in range(n):
        arr[i] = output[i]

# Radix Function
def radix_sort(arr):
    # Find the max number to know num of digits
    max_num = max(arr)

    # Counting sort for every digit
    exp = 1
    # Checking to see if there are digits left to process
    while max_num // exp > 0:
        counting_sort(arr, exp)
        print(arr)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)

# For fun I copied the code from a similar school assignment that had us
# Implement a radix sort using queues. Man I thought this assigment was going
# to be the death of me haha.

# HOMEWORK03 for CS132SP_2025
# import random

# Queue Class borrowed from the textbook
# class Queue:
#     """Queue implementation as a list"""
#     def __init__(self):
#         """Create new queue"""
#         self._items = []

#     # Allows string output for queue class, joins the list of numbers to then it can become a string
#     def __str__(self):
#         result = " ".join(map(str, self._items))
#         return result

#     def is_empty(self):
#         """Check if the queue is empty"""
#         return not bool(self._items)

#     def enqueue(self, item):
#         """Add an item to the queue"""
#         self._items.insert(0, item)

#     def dequeue(self):
#         """Remove an item from the queue"""
#         return self._items.pop()

#     def size(self):
#         """Get the number of items in the queue"""
#         return len(self._items)
    
# def radixSort(radix_queue):
#     # Determines the largest number in the queue and then finds the amount of integers in that number
#     maximum_num = max(radix_queue._items)
#     num_digits_iter = len(str(maximum_num))

#     # Creates a queue for each digit in the range 0-9
#     base_10_queues = [Queue() for i in range(10)]

#     # Print inital radix pass, unsorted
#     print(f'Radix Pass 0: {radix_queue}')

#     # Takes main queue, dequeues number from main queue, 
#     # calculates where to sort it, sorts number into respected queue
#     for j in range(0, num_digits_iter):
#         while not radix_queue.is_empty():
            
#             num = radix_queue.dequeue()
#             # This is a calculation for what digit queue the number will be put into
#             # This goes from the right to the left with the first digit being 0
#             # Example: num = 25
#             #          j = 0
#             #          digit = (num // 10 ** j) % 10 --> this will equal 5
#             # Because 5 is the 0th digit from the right
#             digit = (num // 10 ** j) % 10

#             # Enqueuing to respected queue based on digit
#             base_10_queues[digit].enqueue(num)

#         # Reversed queue order; had issue with final loop order and printing in ascending order.
#         base_10_queues = base_10_queues[::-1]

#         # For each queue in the base_10_queues list it dequeues each number and enqueues into main queue
#         for queue in base_10_queues:
#             while not queue.is_empty():
#                 radix_queue.enqueue(queue.dequeue())

#         # Prints each radix pass, sorting integer by integer
#         print(f'Radix Pass {j + 1}: {radix_queue}')

# # Creates inital array and enqueues each random number into radix_queue 
# # based on the list size
# def createArray(uR, lS):
#     radix_queue = Queue()
#     for i in range(lS):
#         rand_num = random.randrange(0, uR + 1)
#         radix_queue.enqueue(rand_num)

#     return radix_queue

# # Main Function, Asks for user inputs
# def main():
#     user_range = int(input("Enter max range: "))
#     list_size = int(input("Enter list size: "))
#     radix_queue = createArray(user_range, list_size)
#     radixSort(radix_queue)

# main()