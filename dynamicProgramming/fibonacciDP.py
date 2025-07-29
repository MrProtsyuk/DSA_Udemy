# So I had built a fibonacci sequence using recursion but that gave me a time complexity of O(2^n)
# Using dynamic programming I am now able to use that recursion paired with memoization to get the
# time complexity down to O(n).
def fibonacci(num, cache):
    if num in cache:
        print("Used Dynamic Programming!")
        return cache[num]
    if num < 2:
        return num
    else:
        print("Storing values...")
        cache[num] = fibonacci(num - 1, cache) + fibonacci(num - 2, cache)
    return cache[num]

# Extra function I added to avoid using a global variable
def cachePass(num, cache):
    result = fibonacci(num, cache)
    print(f"The fibonacci squeence adds up to {result} when given the input of {num}")

def main():
    cache = {}
    cachePass(5, cache)
    cachePass(6, cache)

main()