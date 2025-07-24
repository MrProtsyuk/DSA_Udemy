# Rotate array Problem
# Given an integer array nums,
# rotate the array to the right by k steps,
# where k is non-negative.

# Initial Brute Force method
def rotateArr(arr, k):
    for i in range(0, k):
        endVal = arr.pop()
        arr.insert(0, endVal)
        
    return arr

# This solution has a time complexity of 0(k x n) Why?
# I am looping through the array and inserting, causing me to loop through again

#  Better Solution
def rotateArr2(arr, k):
    n = len(arr)
    # Handles cases where k > n
    # If K is too large, this handles it unlike the previous solution
    k = k % n

    # This function swaps elements from both ends of the array
    # Moving inwards
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Reverses the entire array
    reverse(0, n-1)
    # Reverses the first k elements
    reverse(0, k-1)
    # Reverses the rest
    reverse(k, n-1)

    return arr

# Time Complexity: 0(n) Why?
# Each call to reverse(start, end) performs about ~val/2 swaps
# if you add them up it is about n


solution = rotateArr([1,2,3,4], 1)
print(solution)

solution2 = rotateArr2([1, 2, 3, 4, 5, 6, 7], 3)
print(solution2)