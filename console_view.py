from __future__ import print_function

from board import *
from tictactoe import *


def show_board(board):
    """
    Board is square matrix.
    Renders board as text, with row and column headers.
    e.g.
      | 0 | 1 | 2 |
    ---------------
    0 | X | O |   |
    ---------------
    1 | O | O | O |
    ---------------
    2 | X | X |   |
    ---------------
    """
    print("  ", end="")
    for col_pos in range(len(board)):
        print("| %s " % (col_pos), end="")
    print("|")
    print("-----" * len(board))
    row_pos = 0
    for row in board:
        print("%d " % (row_pos), end="")
        for square in row:
            print("| %s " % (square), end="")
        row_pos += 1
        print("|")
        print("-----" * len(board))

def get_player_move(player, board):
    while True:
        try:
            player_move = raw_input("%s's turn. Enter a row, column number - e.g. 1,1 > " % (player))
            (row, column) = [(int)(num.strip()) for num in player_move.split(",")]
            if is_illegal_move((row, column), board):
                print("You can't place %s at (%d,%d)." % (player, row, column))
                continue
            return (row, column)
        except (KeyboardInterrupt, EOFError):
            print("!!")
            print("Program interrupted.  Exiting..")
            exit()
        except Exception as e:
            print("Invalid input.  Try again.")
            continue
