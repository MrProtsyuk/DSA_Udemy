# Given two strings, return true or false if the the 
# first string can be constructed using the second
# Each letter in the second can only be used once in the first

# Time Complexity: O(n + m) Why?
# Because it iterates through both strings once
# Space Complexity: O(n) Why?
# It uses a dictionary to store the count of letters in the second string, which can grow up to the size of the second string in the worst case

def canConstruct(str1, str2):
    # since str2 is the one in which we will be comparing, we will make the dictionary based on its letters
    # Counting how times each letter appears.
    str2_letters = {}

    # First loop, popluates the dictionary with necessary keys and values.
    for char in str2:
        # If the char is already in the dictionary, increment by one
        if char in str2_letters:
            str2_letters[char] += 1
        # Else, set the value of the key to one
        else:
            str2_letters[char] = 1

    # Second Loop, iterates through str1 using up the letters from str2
    for char in str1:
        # If the char is not in the dicitonary, False
        if char not in str2_letters or str2_letters[char] == 0:
            return False
        # Else, decrement the value of the char in the str2 dictionary
        str2_letters[char] -= 1

    # If you made it through the str1 without running out of letter in str2 dictionary
    # Return true
    return True

solution = canConstruct("aa", "aab")
print(solution)

def canConstruct2(str1, str2):
    for c in set(str1):
        if str1.count(c) > str2.count(c):
            return False
    return True

solution2 = canConstruct2("aa", "aab")
print(solution2)