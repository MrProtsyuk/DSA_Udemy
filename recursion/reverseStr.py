# This is a function that implements recursion to reverse a string
# Time complexity: O(n^2) Why?
# You call the function n times recursively per character
# String concatenation is O(k). O(n * k) = O(n^2)
# This is a better way to do this with iteration and avoid using concatenation
# but the purpose of this exercise was to do it with recursion 

def reverseStr(rev_str, user_list, count):
    if count == len(user_list) + 1:
        return rev_str
    else:
        letter = user_list[-count]
        rev_str = rev_str + letter
        count += 1
        return reverseStr(rev_str, user_list, count)

def main():
    count = 1
    rev_str = ""
    userStr = str(input("Enter anything: "))
    user_list = list(userStr)
    result = reverseStr(rev_str, user_list, count)
    print(result)
main()