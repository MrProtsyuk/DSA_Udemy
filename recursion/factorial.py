# A simple factorial calculator using recursion
# Time complexity: O(n) Why?
# Function makes one recursive call for each decrement of num
# There is a way to make this O(1) but that avoids using recursion altogether
# Which is not the purpose of this code.
# But I will leave that code below commented out
# def factorial(num):
#     val = 1
#     for i in range(2, num + 1):
#         val *= i
#     return val

# def main():
#     userNum = int(input("Enter a number: "))
#     result = factorial(userNum)
#     print(f"{userNum}! = {result}")

# main()

def factorial(num, val):
    if num == 0:
        return val
    else:
        val = num * val
        return val * factorial(num - 1, val)
   
def main():
    val = 1
    userNum = int(input("Enter a number: "))
    result = factorial(userNum, val)
    print(f"{userNum}! = {result}")

main()
