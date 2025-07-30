# Implementaion of Insertion Sort

#  Borrowed from geeks for geeks: https://www.geeksforgeeks.org/python/python-program-for-insertion-sort/
def insertionSort(nums):
    n = len(nums)
    if n <= 1:
        return print(nums)
    
    for i in range(1, n):
        key = nums[i]
        j = i-1
        # While loop that moves elements greater than key one position ahead
        while j >= 0 and key < nums[j]:
            # Shift elements to the right
            nums[j+1] = nums[j]
            j -= 1
        # Insert the key into the right position
        nums[j+1] = key
    
    return print(nums)

insertionSort([3,2,1,5,4,8])