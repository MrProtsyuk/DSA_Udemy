# Function that puts the two lists together
def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge the two lists while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Implementation of Merge Sort
def mergeSort(nums):
    # Checks to see if the array has only one or zero nodes  
    if len(nums) <= 1:
        return nums
    
    # The first step in our divide conquer
    mid = len(nums) // 2
    # Splitting into two different sides
    left_side = nums[:mid]
    right_side = nums[mid:]

    left_sort = mergeSort(left_side)
    right_sort = mergeSort(right_side)

    return merge(left_sort, right_sort)

# Test the function
print(mergeSort([3, 6, 8, 1, 11, 99, 88, 498, 3, 4, 4, 0]))