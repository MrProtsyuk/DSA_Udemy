# Two Sum Problem
# Time Complexity: O(n) Why?
# Because it iterates through the array once using a hashmap for lookups

def two_sum(nums, target):
    # Creating a hashmap so then you can compare values
    num_map = {}

    # Using a for loop to iterate over each value in the nums arr
    # Using enumerate because it returns both the index and the value of each element as you loop
    # Automatically giving you both i and num
    for i, num in enumerate(nums):
        # The value that will be compared in num_map
        # Which will help us with finding the two values that equal the target
        complement = target - num

        # If this complement value is found, 
        # return index of the number stored, and the current index 
        if complement in num_map:
            return [num_map[complement], i]
        
        # Storing index in num map
        num_map[num] = i

    # if there is no solution
    return "No solution found"

solution = two_sum([2, 7, 11, 15], 27)
print(solution)