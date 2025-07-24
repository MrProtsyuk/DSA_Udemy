# This is a simple array in python
# It is 4*4 which equals 16 bytes of storage
arr = ['a', 'b', 'c', 'd']
print("Original array:", arr)

# Pushing to the array
# Time Complexity: O(1) Why?
# Because it appends to the end without shifting elements
arr.append('e')
print("Array after pushing 'e':", arr)

# Popping from the array
# Time Complexity: O(1) Why?
# Because it removes the last element without shifting others
arr.pop()
print("Array after popping last element:", arr)

# Inserting into the array
# Time Complexity: O(n) Why? 
# Because it may require shifting elements
arr.insert(2, 'x')
print("Array after inserting 'x' at index 2:", arr)

# Removing from the array
# Time Complexity: O(n) Why?
# Because it may require shifting elements
arr.remove('b')
print("Array after removing 'b':", arr)

# Static Array 
# A static array has a fixed size and cannot be resized
static_arr = [1, 2, 3, 4]
print("Static array:", static_arr)

# Dynamic Array
# A dynamic array can grow and shrink in size
dynamic_arr = [5, 6, 7]
print("Dynamic array before resizing:", dynamic_arr)
# Resizing the dynamic array
dynamic_arr.extend([8, 9, 10])
print("Dynamic array after resizing:", dynamic_arr)