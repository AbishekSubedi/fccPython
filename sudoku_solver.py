"""
sudoku_solver.py

A module to solve Sudoku puzzles using a backtracking algorithm.

Classes:
--------
Board
    A class to represent a Sudoku board and provide methods to solve it.

Functions:
----------
solve_sudoku(board)
    Solve the given Sudoku puzzle and print the result.

Example usage:
--------------
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve_sudoku(board)
"""


class Board:
    """
    A class to represent a Sudoku board and provide methods to solve it.

    Attributes:
    -----------
    board : list of list of int
        A 9x9 grid representing the Sudoku board, where 0 represents an empty cell.
    """

    def __init__(self, board):
        """
        Initialize the Board with a 9x9 grid.

        Parameters:
        -----------
        board : list of list of int
            A 9x9 grid representing the Sudoku board, where 0 represents an empty cell.
        """
        self.board = board

    def __str__(self):
        """
        Return a string representation of the board.

        Returns:
        --------
        str
            A string representation of the board, with '*' representing empty cells.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        """
        Find the next empty cell in the board.

        Returns:
        --------
        tuple of int or None
            The row and column indices of the next empty cell, or None if the board is full.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Check if a number is valid in a given row.

        Parameters:
        -----------
        row : int
            The row index.
        num : int
            The number to check.

        Returns:
        --------
        bool
            True if the number is not present in the row, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Check if a number is valid in a given column.

        Parameters:
        -----------
        col : int
            The column index.
        num : int
            The number to check.

        Returns:
        --------
        bool
            True if the number is not present in the column, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Check if a number is valid in the 3x3 square containing the given cell.

        Parameters:
        -----------
        row : int
            The row index of the cell.
        col : int
            The column index of the cell.
        num : int
            The number to check.

        Returns:
        --------
        bool
            True if the number is not present in the 3x3 square, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Check if a number is valid in the given empty cell.

        Parameters:
        -----------
        empty : tuple of int
            The row and column indices of the empty cell.
        num : int
            The number to check.

        Returns:
        --------
        bool
            True if the number is valid in the row, column, and 3x3 square, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        Solve the Sudoku puzzle using backtracking.

        Returns:
        --------
        bool
            True if the puzzle is solved, False if it is unsolvable.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False


def solve_sudoku(board):
    """
    Solve the given Sudoku puzzle and print the result.

    Parameters:
    -----------
    board : list of list of int
        A 9x9 grid representing the Sudoku board, where 0 represents an empty cell.

    Returns:
    --------
    Board
        The Board object representing the solved puzzle, or the unsolvable state.
    """
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard


puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)
