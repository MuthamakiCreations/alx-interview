#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append([''.join(row) for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row+1, N, solutions)
            board[row][col] = '.'

def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    for solution in solutions:
        print("\n".join(solution))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_n_queens(N)
