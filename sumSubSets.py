#Given a sorted array of integers arr and an integer num, find all possible unique subsets of arr that add up to num. Both the array of subsets and the subsets themselves should be sorted in lexicographical order.
#Example
#For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
#sumSubsets(arr, num) = [[1, 4], [2, 3], [5]].
#Input/Output
#[time limit] 4000ms (py)
#[input] array.integer arr
#A sorted array of integers.
#Constraints:
#1 ≤ arr.length ≤ 50,

#-10 ≤ arr[i] ≤ 10.
#[input] integer num





# [output] array.array.integer
# A sorted array containing all possible subsets composed of elements from arr that have a sum of num. It is guaranteed that there are no more than 1000 subsets in the answer.
#Code:
def sumSubsets(arr, num):
    def solve(arr, num, index, path, result):
        if num == 0:
            result.append(path)
            return
        if num < 0:
            return
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i-1]:
                continue
            solve(arr, num - arr[i], i+1, path + [arr[i]], result)
    result = []
    solve(arr, num, 0, [], result)
    return result

print(sumSubsets([1, 2, 3, 4, 5], 5))
