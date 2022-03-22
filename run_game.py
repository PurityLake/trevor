#!/usr/bin/env python3

"""run_game.py
Script to run the game`
"""

import os, sys

import arcade

from trevor.game import Game

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Trevor - Pyweek 33"

if __name__ == "__main__":
    APP_PATH = ""
    if getattr(sys, 'frozen', False):
        APP_PATH = os.path.dirname(sys.executable)
    elif __file__:
        APP_PATH = os.path.dirname(__file__)
    game: Game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, APP_PATH)
    game.setup()
    arcade.run()
