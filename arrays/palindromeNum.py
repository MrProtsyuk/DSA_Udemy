# Implementation of Palindrome Number Leetcode problem
# Initial Brute force method
def palindromNum(x):
    compareArr = []
    arr = list(str(x))
    for i in range(1, len(arr) + 1):
        compareArr.append(arr[-i])
    
    compareNum = int("".join(compareArr))
    if x == compareNum:
        return True
    else:
        return False

print(palindromNum(121))

# Faster way for comparision using python built in quick reverse
def palindromNum2(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False

print(palindromNum2(121))