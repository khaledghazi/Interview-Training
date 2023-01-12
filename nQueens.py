#In chess, queens can move any number of squares vertically, horizontally, or diagonally. The n-queens puzzle is the problem of placing n queens on an n × n chessboard so that no two queens can attack each other.
#Given an integer n, print all possible distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the placement of the n queens, where the solutions are arrays that contain permutations of [1, 2, 3, .. n].
#The number in the ith position of the results array indicates that the ith column queen is placed in the row with that number. In your solution, the board configurations should be returned in lexicographical order.
#Example
#For n = 1, the output should be
#nQueens(n) = [[1]].
#For n = 4, the output should be
#nQueens(n) = [[2, 4, 1, 3],
#              [3, 1, 4, 2]]
#Input/Output
#[time limit] 4000ms (py)
#[input] integer n
#Constraints:
#1 ≤ n ≤ 10.
#[output] array.array.integer
#It is guaranteed that there is no more than one correct solution for the given n.
#Code:
def nQueens(n):
    def is_valid(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if there is a queen in the same diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, row):
        if row == n:
            # We have placed all queens, so we found a valid solution
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append(j+1)
                        break
            solutions.append(solution)
            return

        for col in range(n):
            if is_valid(board, row, col):
                # Place the queen in the current cell
                board[row][col] = 1
                # Recursively try to place the rest of the queens
                solve(board, row+1)
                # Backtrack and remove the queen from the current cell
                board[row][col] = 0

    # Initialize the board with all cells empty
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Store the solutions in a list
    solutions = []
    # Start the recursive backtracking from the first row
    solve(board, 0)
    return solutions

print(nQueens(4))
