#!/usr/bin/env python3

"""run_game.py
Script to run the game`
"""

import arcade

from trevor.game import Game

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_TITLE: str = "Trevor - Pyweek 33"

if __name__ == "__main__":
    game: Game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
