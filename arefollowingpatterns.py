#Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
#Example
#For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be areFollowingPatterns(strings, patterns) = true;
#For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be areFollowingPatterns(strings, patterns) = false.
#Input/Output
#[execution time limit] 4 seconds (py3)
#[input] array.string strings
#An array of strings, each containing only lowercase English letters.
#Guaranteed constraints:
#0 ≤ strings.length ≤ 105,
#1 ≤ strings[i].length ≤ 10.
#[input] array.string patterns
#An array of pattern strings, each containing only lowercase English letters.
def areFollowingPatterns(strings, patterns):
    return len(set(zip(strings, patterns))) == len(set(strings)) == len(set(patterns))  

print(areFollowingPatterns(["cat", "dog", "dog"], ["a", "b", "b"]))