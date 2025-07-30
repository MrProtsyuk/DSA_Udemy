# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    # Checking to see if the list is empty
    if not prices:
        return 0
    
    # Starting with the first days price
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # If the next days price is lower than the previous days, update the min price
        if price < min_price:
            min_price = price
        # Else if the profit made by selling today is greater than any profit seen, update profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit