# Implementation of quick sort
# Used some help from ChatGPT to understand what exactly was going on under the hood

def quick_sort(arr):
    # Calls helper function, 0 means Low and len(arr) - 1 means High
    # Meaning that we are sorting the full array
    _quick_sort(arr, 0, len(arr) - 1)

def _quick_sort(arr, low, high):
    # ensures that we don't process single-element or empty sections
    if low < high:
        # Partition the array to find the index, correct place
        pivot_index = partition(arr, low, high)
        # recursion on the left of pivot
        _quick_sort(arr, low, pivot_index - 1)
        # recursion on the right of the pivot
        _quick_sort(arr, pivot_index + 1, high)

# Partition function
def partition(arr, low, high):
    # choosing the last element of our partition
    pivot = arr[high]
    # tracks the bounds of the less than pivot section
    i = low - 1

    # loop through pivot section, swapping when pivot is >= j
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # returns index of pivot, now in its sorted position
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print(arr)