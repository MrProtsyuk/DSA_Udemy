# Implementation of Bubble sort 

def bubbleSort(nums):
    # Nested loops is what gives us that bitter O(n^2)
    # Had to use some interesting steppage with python, JS can just do the length of arrays.
    for i in range(len(nums) - 1, 0 , -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return print(nums)

bubbleSort([17, 66, 3, 90, 2, 1])
     