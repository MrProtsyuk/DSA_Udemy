# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# This is my initial brute force method, but sadly it fails because it does not take into consideration
# the maximum amount of money. Even though it pass the test cases.
def robHouse(nums):
    output = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            output = output + nums[i]
    return print(output)

robHouse([1,2,3,1])

# This is a better solution using Dynamic Progamming
def robHouse2(nums):
    # Checking to see if the array is empty
    if not nums:
        return 0
    # Checking to see if the array has one or two items in it
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    # Populating a list full of zero values for dp, adding the first two values
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Looping through the rest of the array, since we already have the first 2 values, we start at index 2
    for i in range(2, len(nums)):
        # This does a similar check to what is above. 
        # You can skip: i-1
        # Or you can rob the house: nums[i] + [i-2]
        dp[i] = max(dp[i-1], nums[i] + dp[i - 2])

    return dp[-1]

robHouse2([1,2,3])
    
