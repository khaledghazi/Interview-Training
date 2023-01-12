#Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.
#Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, find all the possible words from words that can be formed on the board.
#Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.
#Example
#For
#board = [['R', 'L', 'D'],
#         ['U', 'O', 'E'],
#         ['C', 'S', 'O']]
#and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
#wordBoggle(board, words) = ["CODE", "RULES"].
#Input/Output
#[time limit] 4000ms (py)
#[input] array.array.char board
#A 2-dimensional array of uppercase English characters representing a rectangular Boggle board.
#Constraints:
#2 ≤ board.length ≤ 4,
#2 ≤ board[i].length ≤ 4.
#[input] array.string words
#An array of unique English words consisting only of uppercase characters.
#Constraints:
#0 ≤ words.length ≤ 100,
#3 ≤ words[i].length ≤ 16.
#[output] array.string
#An array of all the words from words that can be formed on the Boggle board.
#Code:
def wordBoggle(board, words):
    r = []
    for word in words:
        if canBoggle(board,word):
            r.append(word)
    return sorted(r)

def canBoggle(board, word, used = []):
    if len(word) == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) not in used and board[i][j] == word[0]:
                if len(used)==0 or (abs(used[-1][0] - i)<=1 and abs(used[-1][1] - j)<= 1):
                    if canBoggle(board,word[1:],used + [(i,j)]):
                        return True
    return False        

print(wordBoggle([['R', 'L', 'D'], ['U', 'O', 'E'], ['C', 'S', 'O']], ["CODE", "SOLO", "RULES", "COOL"]))

