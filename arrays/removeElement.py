# Implementation of Remove element Leetcode problem

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

print(removeElement([2,3,3,2], 3))