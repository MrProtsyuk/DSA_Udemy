# Implementation of counting sort
# Counting sort is similar to radix because it is non comparision based.
# It is best for sorting integers 

# How it works is that it counts how many times each number appears and then
# using that count to place elements in the correct positions

def counting_sort(arr):
    if not arr:
        return []
    
    # Nedd to know the maximum value to size our counting array
    max_val = max(arr)
    #  +1 because we need to include the index of the max number
    count = [0] * (max_val + 1)

    # Count occurrences going through the original array and incrementing the count
    for num in arr:
        count[num] += 1

    # Build the sorted output 
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
        print(output)

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)