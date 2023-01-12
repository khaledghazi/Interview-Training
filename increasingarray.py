#You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

#Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

#Example

#    For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.

#    The initial array is already strictly increasing, so no actions are required.

#   For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.

#    By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

#    For numbers = [13, 31, 30], the output should be solution(numbers) = false.
#        The initial array elements are not increasing.
#        By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
#        By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
#        By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
#    So, it's not possible to obtain a strictly increasing array, and the answer is false.

#Input/Output

#    [time limit] 4000ms (py)

#    [input] array.integer numbers

#    An array of non-negative integers.

#    Constraints:
#    1 ≤ numbers.length ≤ 105,
#    0 ≤ numbers[i] ≤ 109.

#    [output] boolean

#    true if it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing, false otherwise.

#Code:
def solution(numbers):
    # Initialize a variable to store the number of swaps that have been performed
    swaps = 0

    # Iterate over all elements of the array except the last one
    for i in range(len(numbers) - 1):
        # If the current element is greater than or equal to the next one
        if numbers[i] >= numbers[i + 1]:
            # Increment the number of swaps
            swaps += 1
            # If the number of swaps is greater than 1
            if swaps > 1:
                # Return false
                return False
            # If the current element is greater than 10
            if numbers[i] > 10:
                # If the last digit of the current element is greater than the first digit of the next element
                if numbers[i] % 10 > numbers[i + 1] // 10:
                    # Return false
                    return False
            # If the next element is greater than 10
            if numbers[i + 1] > 10:
                # If the last digit of the current element is greater than the first digit of the next element
                if numbers[i] % 10 > numbers[i + 1] // 10:
                    # Return false
                    return False

    # Return true
    return True