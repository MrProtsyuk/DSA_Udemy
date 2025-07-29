# This is an implementation of the fibonacci sequence using recursion
# Time Complexity: O(2^n) Why?
# The function makes two recursive calls, and this creates a binary tree of calls that grow exponentially
# You can make this faster and better in regards to time complexity by using iteration
# The time complexity of that code will come down to O(n)
# def fibonacci_Iter(num):
#     if num < 2:
#         return num
#     a, b = 0, 1
#     for i in range(2, num + 1):
#         a, b = b, a + b
#     return b

def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    userNum = int(input("Enter a number: "))
    result = fibonacci(userNum)
    print(f"The fibonacci squeence adds up to {result} when given the input of {userNum}")

main()
