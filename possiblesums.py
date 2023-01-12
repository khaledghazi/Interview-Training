#You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

#Example

#For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
#solution(coins, quantity) = 9.

def solution(coins, quantity):
    sums = {0}
    for coin, amount in zip(coins, quantity):
        sums |= {coin * i + s for i in range(1, amount + 1) for s in sums}
    return len(sums) - 1

print(solution([10, 50, 100], [1, 2, 1]))
