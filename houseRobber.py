#You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.
#Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.
#Example
#For nums = [1, 1, 1], the output should be
#houseRobber(nums) = 2.
#The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.
#Input/Output
#[time limit] 4000ms (py)
#[input] array.integer nums
#An array representing the amount of money that each house on the street has.
#Constraints:
#0 ≤ nums.length ≤ 100,
#0 ≤ nums[i] ≤ 500.
#[output] integer
#The maximum amount of money that you can rob in one night without triggering an alarm.
#Code:
def houseRobber(nums):
    # Initialize an array to store the maximum amount of money that can be robbed from each house
    max_money = [0] * (len(nums) + 1)

    # Iterate over all houses from 0 to the last one
    for i in range(len(nums)):
        # The maximum amount of money that can be robbed from the current house is the maximum of:
        # - the maximum amount of money that can be robbed from the previous house
        # - the maximum amount of money that can be robbed from the previous two houses plus the money in the current house
        max_money[i + 1] = max(max_money[i], max_money[i - 1] + nums[i])

    # Return the maximum amount of money that can be robbed from the last house
    return max_money[-1]

#print(houseRobber([1, 1, 1]))  # 2
#print(houseRobber([2, 3, 2]))  # 3
#print(houseRobber([1, 2, 3, 1]))  # 4
#print(houseRobber([2, 7, 9, 3, 1]))  # 12
print(houseRobber([5, 1, 1, 5]))  # 10

