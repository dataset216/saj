def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []
    cols = [False] * n
    diagonals1 = [False] * (2 * n - 1)
    diagonals2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            solution = ["".join(row) for row in board]
            solutions.append(solution)
            return

        for col in range(n):
            if not is_threatened(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    def is_threatened(row, col):
        return cols[col] or diagonals1[row + col] or diagonals2[row - col + n - 1]

    def place_queen(row, col):
        board[row][col] = "Q"
        cols[col] = True
        diagonals1[row + col] = True
        diagonals2[row - col + n - 1] = True

    def remove_queen(row, col):
        board[row][col] = "."
        cols[col] = False
        diagonals1[row + col] = False
        diagonals2[row - col + n - 1] = False

    backtrack(0)
    return solutions


# Example usage:
n = 4
solutions = solve_n_queens(n)

for solution in solutions:
    print("\n".join(solution))
    print()
