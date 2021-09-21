from tkinter import *
from tkinter import ttk

import game

DEFAULT_BOARD_SIZE = 3
ICONS = ["X", "O"]

human_player = [True, False]

current_player = 0


game_board = game.Game(DEFAULT_BOARD_SIZE)

playing = True
while playing:
    for row in game_board.board:
        print(row)
    move = input("Enter your move: ")
    game_board.board[int(move[0])][int(move[1])] = ICONS[current_player]
    current_player = (current_player + 1) % 2
    done = game_board.finished()
    if done:
        print(f"{done} Wins")
        playing = False

# root = Tk()
