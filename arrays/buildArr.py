class MyArray:
    def __init__(self):
        self.arr = [None] * 4
        self.length = 0

    def __str__(self):
        return str(self.arr[:self.length])

    def get(self, index):
        return self.arr[index]

    def push(self, value):
        self.arr[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.arr[self.length]

myArray = MyArray()
print(myArray)
myArray.push('a')
myArray.push('b')
myArray.push('c')
myArray.push('d')
myArray.pop()
# This will not work as expected since the array is static
print(myArray)
