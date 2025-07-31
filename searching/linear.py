# This is an Implementation of a linear search

# all this is doing is just looping haha
def linearSearch(arr, key):
    for i in arr:
        if i == key:
            return True
    
    return False

result = linearSearch([2, 5, 66, 8127, 90, 543], 90)
print(f"Does key exist in array? {result}")