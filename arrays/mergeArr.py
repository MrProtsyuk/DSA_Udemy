# Merge sorted arrays
# Time Complexity: O(n + m) Why?
# Because it iterates through both arrays once

import heapq

# Use this method for interview questions, it will help you walk through the problem
def merge_sorted_arrays(arr1, arr2):
    # Initial Check to see if arrays are populated
    if len(arr1) == 0:
        return print(arr2)
    if len(arr2) == 0:
        return print(arr1)
    
    # Creating the final list
    mergedArr = []
    # Chained assignment trick in python
    i = j = 0

    # Checking to see if the assigned variables are less than the len of the arrays
    # Will fail when one or the other exceeds the condition
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergedArr.append(arr1[i])
            i += 1
        
        else:
            mergedArr.append(arr2[j])
            j += 1
    
    # This will then append an stragler elements
    while i < len(arr1):
        mergedArr.append(arr1[i])
        i += 1
    while j < len(arr2):
        mergedArr.append(arr2[j])
        j += 1

    print(mergedArr)


# Use this method if you are lazy lol
def merge_sorted_arrays_heap(arr1, arr2):
    # Use heapq to merge two sorted arrays
    mergedArr = list(heapq.merge(arr1, arr2))
    print(mergedArr)

merge_sorted_arrays([1, 3, 5], [2, 4, 6])
merge_sorted_arrays_heap([1, 3, 5], [2, 4, 6])
