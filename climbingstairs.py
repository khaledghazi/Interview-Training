#You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.
#Example
#For n = 4 and k = 2, the output should be
#climbingStairs(n, k) = [[1, 1, 1, 1],
#                       [1, 1, 2],
#                       [1, 2, 1],
#                       [2, 1, 1],
#                       [2, 2]]

def climbingStairs(n, k):
    if n == 0:
        return [[]]
    if n < 0:
        return []
    result = []
    for i in range(1, k + 1):
        for j in climbingStairs(n - i, k):
            result.append([i] + j)
    return result


print(climbingStairs(4, 2))