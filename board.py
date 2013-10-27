__author__ = 'John Duprey'

EMPTY = " "

def create_board(size):
    """
    The game board is represented as a square matrix.
    """
    board = []
    for i in range(size):
        board.append([EMPTY, EMPTY, EMPTY])
    return board

def mark_board(board, marker, row, column):
    board[row][column] = marker
