# Given an integer array nums, 
# return true if any value appears at 
# least twice in the array,
#  and return false if every element is distinct.

# This is my Initial Brute force method
def containsDup(nums):
    num_map = {}
    for i, num in enumerate(nums):
        if num in num_map:
            num_map[num] = True
        else:
            num_map[num] = False
    
    for i in num_map:
        if num_map[i] == True:
            return True
    
    return False

# This is the common solution online
# Time Complexity: 0(n) Why?
# it has iterate through the array
# Space Complexity: 0(n) Why?
# In the worst case, when there are no duplicates
def containsDup2(nums):
    # A set that keeps track of numbers we have seen
    seen = set()
    # Common for loop that iterates through the given array
    for num in nums:
        # if the number we have from num is already in the set
        # we just return true and quit the program
        if num in seen:
            return True
        # If not, we add it to the set
        seen.add(num)
    # If worst comes to worst, we return false
    # after iterating through the entire array.
    return False


solution = containsDup2([1,2,3,1])
print(solution)