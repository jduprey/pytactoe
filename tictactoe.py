__author__ = 'John Duprey'

from board import *

def is_illegal_move(move, board):
    """
    Returns true if the tuple, move, containing (row, column) is not a valid location.
    """
    (row, column) = move
    try:
        valid_range = range(len(board))
        if row not in valid_range or column not in valid_range:
            return True
        return board[row][column] != EMPTY
    except:
        return True

def all_the_same(line):
    if line[0] != EMPTY:
        if line.count(line[0]) == len(line):
            return line[0]
    return EMPTY

def winner(board):
    # check for all of a kind in a row
    for row in board:
        win = all_the_same(row)
        if win != EMPTY:
            return win

    # check for all of a kind in a column
    for col_pos in range(len(board)):
        col = [row[col_pos] for row in board]
        win = all_the_same(col)
        if win != EMPTY:
            return win

    # check diagonals

    # 0,0 to #,#
    diag = [board[i][i] for i in range(len(board))]
    win = all_the_same(diag)
    if win != EMPTY:
        return win

    # #,0 to 0,#
    reverse = [board[i] for i in range(len(board) - 1, -1, -1)]
    diag = [reverse[i][i] for i in range(len(reverse))]
    win = all_the_same(diag)
    if win != EMPTY:
        return win

    return EMPTY


def game_over(board):
    winning_player = winner(board)
    if winning_player == EMPTY:
        for row in board:
            if EMPTY in row:
                return False
    return True
