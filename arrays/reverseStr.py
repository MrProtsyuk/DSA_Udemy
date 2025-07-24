# Reverse a string in python,
# Time Complexity: O(n) Why?
# Because it iterates through the string once

def main():
    # Reverse a string in python and print it
    str = "hello"
    # Expected out put: olleh
    newStr = []
    # This works by using the start, stop, step parameters of the range function
    for i in range(len(str) - 1, -1, -1):
        newStr.append(str[i])
    
    print("Reversed string:", ''.join(newStr))


main()