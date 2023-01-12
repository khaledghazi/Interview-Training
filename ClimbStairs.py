def solution(n):
    # Initialize an array to store the number of ways to reach each step
    ways = [0] * (n+1)
    # The number of ways to reach the first step is 1
    ways[0] = 1
    
    for i in range(1, n+1):
        # The number of ways to reach the current step is the sum of the number of ways to reach the previous two steps
        ways[i] = ways[ i -1] + ways [i -2]
     # Return the number of ways to reach the n-th step  
    return ways[n]

print(solution(4))