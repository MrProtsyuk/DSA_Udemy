# Implementation of Selection Sort

def selectionSort(nums):
    # Nested loop gives us that O(n^2)
    for i in range(len(nums)):
        minimum = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[i], nums[minimum] = nums[minimum], nums[i]
    
    return print(nums)

selectionSort([3, 6, 7, 88, 1, 2])