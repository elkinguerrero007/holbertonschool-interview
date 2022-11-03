#!/usr/bin/python3
"""
Solving N Queens problem using backtracking algorithm
- 0x0C-nqueens module
- Holberton School
- Python Core - 0x0C
- N Queens
- Author: JuanDAC
- Date: July 2022
- File: 0x0C-nqueens.py
"""
from sys import argv, exit


def is_safe(y, x, board):
    """
    Method:
        is_safe(n: int, y: int, x: int, board: list) -> bool
    Description:
        This method checks if a queen can be placed on
        a given board at a given position. It checks if
        the queen is attacking any other piece on the board.
    Args:
        y {int}
            current row
        x {int}
            current column
        board {List[int]}
            current board
    Print:
        - True if the queen can be placed on the board, False otherwise
    Return:
        - bool
    """

    for cell in board:
        if x == cell[1]:
            return False
        if y - x == cell[0] - cell[1]:
            return False
        if x - cell[1] == cell[0] - y:
            return False
    return True


def nqueens(n, y, board):
    """
    Method:
        nqueens(n: int, y: int, board: list) -> void
    Description:
        This method is a recursive method that
        places n queens on an n by n board so
        that no queens are attacking any other
        piece on the board. It uses backtracking
        to find a solution.
    Args:
        n {int}
            number of queens
        y {int}
            current row
        board {List[int]}
            current board
    Print:
        - All possible solutions for n queens on an n by n board
    Return:
        - void
    """

    for x in range(n):
        if is_safe(y, x, board):
            board.append([y, x])
            if y == n - 1:
                print(board)
                del board[-1]
                break
            nqueens(n, y + 1, board)
            del board[-1]


if __name__ == '__main__':
    """
    Main guard - check for correct number of arguments and call nqueens
    """
    n = 0
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except Exception:
        print('N must be a number')
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(n, 0, [])
