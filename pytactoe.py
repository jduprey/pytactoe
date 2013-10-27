from __future__ import print_function
from random import choice

EMPTY = " "

def init_board(size):
    board = []
    for i in range(size):
        board.append([EMPTY, EMPTY, EMPTY])
    return board


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


def show_board(board):
    print("  ", end="")
    for col_pos in range(len(board)):
        print("| %s " % (col_pos), end="")
    print("|")
    print("-----" * board_size)
    row_pos = 0
    for row in board:
        print("%d " % (row_pos), end="")
        for square in row:
            print("| %s " % (square), end="")
        row_pos += 1
        print("|")
        print("-----" * board_size)


def get_player_move(player):
    while True:
        try:
            player_move = raw_input("[%s's turn](row #, column #)> " % (player))
            (row, column) = [(int)(num.strip()) for num in player_move.split(",")]
            return (row, column)
        except:
            print("Invalid input.  Try again.")
            continue


def is_illegal_move(move, board):
    (row, column) = move
    return board[row][column] != EMPTY


def game_over(board):
    winning_player = winner(board)
    if winning_player == None:
        for row in board:
            if EMPTY in row:
                return False
    return True


def mark_board(board, player, row, column):
    board[row][column] = player

board_size = 3
board = init_board(board_size)
show_board(board)

players = ["X", "O"]

turn = choice([0, 1])
while not game_over(board):
    turn += 1
    player = players[turn % 2]
    (row, column) = get_player_move(player)
    while is_illegal_move((row, column), board):
        print("You can't place %s at (%d,%d)." % (player, row, column))
        (row, column) = get_player_move(player)
    mark_board(board, player, row, column)
    show_board(board)

winning_player = winner(board)
if winning_player != EMPTY:
    print("Player %s wins!!" % (winning_player))
else:
    print("Stale mate.  Nobody wins.")

