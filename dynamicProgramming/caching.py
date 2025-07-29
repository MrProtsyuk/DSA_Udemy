# Implementing a way to use memoization in this simple function
# This function checks to see if the number is in the directory,
# If yes, then it returns the key without needing to do computation.
# Else, it does the computation and then updates the cache dictionary
def memoizedAddTo80(n, cache):
    if n in cache:
        print("Used Memoization")
        return cache[n]
    else:
        cache[n] = n + 80
        print("Added your number to cache")
        return cache[n]
    
# Extra function I added to avoid using a global variable, why not use a global you might ask?
# My professor once roasted me so hard for using global variables that now I am traumatized
def cachePass(n, cache):
    result = memoizedAddTo80(n, cache)
    print(f"Your number plus 80 = {result}")

# Main function, simple
def main():
    cache = {}
    cachePass(5, cache)
    cachePass(5, cache)
main()