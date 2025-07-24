# Maximum Subarray Problem
# Time Complexity: O(n) Why?
# Because it iterates through the array once

# This uses Kadane's algorithm to find the maximum subarray sum
# How it works:
# As you move through the array, you keep track of the maximum 
# sum of the subarray ending at the current position.
# As well as the maximum sum found so far (global maximum).

def max_subArray(nums): #47ms
    # Using chained assignment in python
    max_current = max_global = nums[0]
    
    # Iteration through the rest of the array
    # For each num it is going to decide if it should start 
    # a new subarray, or extend the current one (max_current + num)
    # Then it will update the global_max if the current one is better
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Maximum Subarray Problem with elements
# Time Complexity: O(n) Why?
# Because it iterates through the array once and keeps track of indices

def max_subArray_with_elements(nums): 
    # Using chained assignment in python
    max_current = max_global = nums[0]
    # This is to track subarray indices
    start = end = s = 0

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            s = i
        else:
            max_current += nums[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i

    return max_global, nums[start:end+1]

# If you want a super duper fast way to do it use this code (0ms)
def maxSubArray(nums):
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum

solution1 = max_subArray([-2,1,-3,4,-1,2,1,-5,4])
solution2, arr = max_subArray_with_elements([-2,1,-3,4,-1,2,1,-5,4])
print(solution1)
print(solution2, arr)
