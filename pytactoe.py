__author__ = 'John Duprey'

from random import choice

from board import *
from console_view import *
from tictactoe import *

board_size = 3
board = create_board(board_size)
show_board(board)
players = ["X", "O"] # Tic Tac Toe has 2 players, "X" and "O"
turn = choice([0, 1]) # Determine who gets to go first, X or O, randomly
while not game_over(board):
    turn += 1
    player = players[turn % 2]
    (row, column) = get_player_move(player, board)
    mark_board(board, player, row, column)
    show_board(board)

winning_player = winner(board)
if winning_player != EMPTY:
    print("Player %s wins!!" % (winning_player))
else:
    print("Stale mate.  Nobody wins.")

