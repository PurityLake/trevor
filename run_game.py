#!/usr/bin/env python3

import arcade

from trevor.game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Trevor - Pyweek 33"

if __name__ == "__main__":
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()