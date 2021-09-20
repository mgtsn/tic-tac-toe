from tkinter import *
from tkinter import ttk

import game

DEFAULT_BOARD_SIZE = 3
ICONS = [" ", "X", "O"]

current_player = 1

game_board = game.Game(DEFAULT_BOARD_SIZE)
print(game_board.finished())

root = Tk()
