# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Time complexity: O(n) because of the loop

# This is similar to the fibonacci problem

def climbingStairs(n):
    # Our first base case: 1 will always equal 1 step
    if n == 1:
        return 1
    # Our second base case: 2 will always equal 2 steps, either 1+1 or just 2 
    if n == 2:
        return 2

    # Ways to reach n-1: One step before the current
    one_step_before = 2
    # Ways to reach n-2: Two steps before the current
    two_steps_before = 1

    for i in range(3, n+1):
        # At each step the total ways to reach current = the sum of the ways to reach n-1 and n-2
        # Shifting the two tracking variables forward
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return print(one_step_before)

climbingStairs(3)