# Given an array, tell me the first recurring character
# Initial Method
# This is a solution to find the first recurring character in an array
# Time Complexity: O(n) Why?
# It iterates through the array once
# Space Complexity: O(n) Why?
# It uses a dictionary to store seen numbers, which can grow up to the size of the input array in the worst case
def recurringCheck(arr):
    num_table = {}
    for i, num in enumerate(arr):
        if num in num_table:
            return f"The first recurring char is {num}"
        num_table[num] = i
    
    return f"There are no recurring chars in the arr"
        
solution = recurringCheck([2,1,3,4,2,1,5,7,1])
print(solution)

# This is a more optimized solution using a set
# Time Complexity: O(n) Why?
# It iterates through the array once
# # Space Complexity: O(n) Why?
# It uses a set to store seen numbers, which can grow up to the size of the input array in the worst case
def recurringCheck2(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return f"The first recurring char is {num}"
        seen.add(num)
    
    return f"There are no recurring chars in the arr"
solution2 = recurringCheck2([2,1,3,4,2,1,5,7,1])
print(solution2)
