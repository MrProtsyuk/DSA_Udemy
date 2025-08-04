# Implementation of the Fruit Into Baskets problem using a sliding window approach.
def total_fruit(fruits):
    left = 0
    right = 0
    basket = {}
    max_fruits = 0

    while right < len(fruits):
        # Add the current fruit to the basket
        if fruits[right] in basket:
            basket[fruits[right]] += 1
        else:
            basket[fruits[right]] = 1

        # If we have more than two types of fruits, shrink the window from the left
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, right - left + 1)
        right += 1

    return max_fruits

print(total_fruit([1, 2, 1]))  # Example usage, should return 3