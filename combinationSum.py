#Given an array of integers a and an integer sum, find all of the unique combinations in a that add up to sum.
#The same number from a can be used an unlimited number of times in a combination.
#Elements in a combination (a1 a2 … ak) must be sorted in non-descending order, while the combinations themselves must be sorted in ascending order.
#If there are no possible combinations that add up to sum, the output should be the string "Empty".
#Examples:
#For a = [2, 3, 5, 9] and sum = 9, the output should be
#solution(a, sum) = "(2 2 2 3)(2 2 5)(3 3 3)(9)".
#For a = [2, 3, 5, 9] and sum = 15, the output should be
#solution(a, sum) = "(2 2 2 2 2 2 3 3)(2 2 2 2 2 5 5)(2 2 2 3 9)(2 2 5 5 3)(2 3 3 3 3 3)(2 3 3 5 5)(2 3 9 9)(2 5 5 5 3)(3 3 3 3 5)(3 3 3 9)(3 3 5 5 3)(3 5 5 5 5)(5 5 5 9)(9 9 9)".
#For a = [2, 3, 5, 9] and sum = 1, the output should be
#solution(a, sum) = "Empty".
#Input/Output
#[time limit] 4000ms (py)
#[input] array.integer a
#A sorted array of positive integers.
#Constraints:
#2 ≤ a.length ≤ 11,
#1 ≤ a[i] ≤ 9.
#[input] integer sum
#Constraints:
#1 ≤ sum ≤ 25
#[output] string
#All possible combinations that add up to a given sum, or "Empty" if there are no possible combinations.
#Code:
def solution(a, sum):
    # Sort the elements in a and remove duplicates
    a = sorted(set(a))
    # Initialize an empty list to store the combinations
    res = []
    # Define the search function
    def search(temp, p, sum):
     # If p is equal to the length of a   
        if len(a) == p:
    # If sum is 0, add the current combination to res
            if sum == 0:
                res.append(" ".join([str(n) for n in temp]))
    # If p is less than the length of a
        else:
     # Iterate over all possible values of i from sum // a[p] down to 0
            for i in range(sum // a[p], -1, -1):
    # Append i copies of a[p] to temp and call search with p + 1 and sum - i * a[p] as arguments
                search(temp + [a[p]] * i, p + 1, sum - i * a[p])
    # Call search with an empty list, 0, and sum as arguments
    search([], 0, sum)
    # Otherwise, return the combinations in the required format
    return "".join(["("+s+")" for s in res]) if res else "Empty"

print(solution([8, 7, 1],22))