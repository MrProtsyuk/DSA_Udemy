# Implementation of Pascal's Triangle II LeetCode problem

def getRow(int):
    row = [1]  # The first element is always 1
    for k in range(1, int + 1):
        # Calculate the next element using the previous one
        next_element = row[k - 1] * (int - k + 1) // k
        row.append(next_element)
    return row

print(getRow(3))  # Example usage, should return [1, 3, 3, 1]