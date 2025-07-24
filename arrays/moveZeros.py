# Given an integer array nums, move all 0's 
# to the end of it while maintaining the 
# relative order of the non-zero elements.
# Note that you must do this in-place 
# without making a copy of the array.

def moveZeroes(nums):
    # Pointer for the position to place the next non-zero element
    # You maintain a pointer that keeps track of where the next non-zero element should go.
    last_non_zero = 0

    # When you find a non-zero element, you swap it with the pointer element
    # This moves all non-zeero elements to the front and pushes zeros to the back
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    
    return nums
    
    # This function is able to retain the same memory
    # Not returning a new list
    # Time Complexity: O(n) Why?
    # We have to loop through the array once
    # Space Complexity: 0(1) Why?
    # No extra memory is used. 

solution = moveZeroes([0, 3, 9, 21, 0, 9, 0])
print(solution)