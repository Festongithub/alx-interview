#!/usr/bin/env python3

"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
Write a program that solves the N queens problem.
Usage: nqueens N
If the user called the program with the wrong
number of arguments,
print Usage: nqueens N, followed by a new line,
and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
The program should print every possible
solution to the problem
One solution per line
"""

import sys


def print_solution(solution):
    """Gets solution"""
    print([[i, row.index(1)] for i, row in enumerate(solution)])


def is_safe(board, row, col, N):
    """
    check for upper column
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

        return True


def solve_nqueens(board, row, N, solution):
    """
    board row matrix
    """
    if row == N:
        solution.append([row[:] for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solution)
            board[row][col] = 0


def nqueens(N):
    """solve the matrix
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solution = []
    solve_nqueens(board, 0, N, solution)
    for sol in solution:
        print_solution(sol)


def validate_and_run():
    """
    validation
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValuError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == '__main__':
    validate_and_run()
