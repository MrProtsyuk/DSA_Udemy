# Implementation of Merge Sorted Array leet code problem 
# Not meant to return anything
def merge(nums1, m, nums2, n):
    # Creating pointers to the last valid elements in each array
    # Since the arrays are already sorted we can start from the end and work our way forward
    i = m - 1
    j = n - 1
    # Pointer to the end of nums1
    k = m + n - 1

    # Comparing nums1[i] and nums2[j] and whichever is larger we place it at nums1[k] and move the pointer back
    # We also move k back as well
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are any leftovers in nums2, add them to nums1[k], moving both pointers back until the nums2 is empty
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

