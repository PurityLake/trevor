"""player.py
Contains Player class that implements logic and
drawing functionality for the game
"""

import os
import sys
from typing import Tuple
import arcade

MIN_ROT: int = -25
MAX_ROT: int = 25
CHANGE_ROT: float = 3.5
FILENAME: str = os.path.join("assets", "images", "steve.png")
SPEED_X: int = 5
SPEED_Y: int = 5
CELL_WIDTH: int = 16

class Player(arcade.Sprite):
    """Player
    Contains the logic and drawing functionality for the player
    in the Trevor game
    """

    MAX_HEALTH: int = 5

    def __init__(self):
        app_path = ""
        if getattr(sys, 'frozen', False):
            app_path = os.path.dirname(sys.executable)
        elif __file__:
            app_path = os.path.dirname(__file__)

        filename = os.path.join(app_path, FILENAME)
        super().__init__(filename, 1)

        self.moving: bool = False
        self.vec: Tuple[int, int] = (0, 0)
        self.rot_dir: int = 1
        self.health: int = 5

        

        self.copy: arcade.Sprite = arcade.Sprite(filename, 1)
        self.copy.set_hit_box(
            [
                (-self.width / 2 + CELL_WIDTH, -self.height / 2),
                (-self.width / 2 + CELL_WIDTH, -self.height / 4),
                ( self.width / 2 - CELL_WIDTH, -self.height / 4),
                ( self.width / 2 - CELL_WIDTH, -self.height / 2)])
        self.set_position(100, 100)

    def on_update(self, delta_time: float = 1 / 60):
        super().update()

        if self.moving:
            self.copy.change_x = SPEED_X * self.vec[0]
            self.copy.change_y = SPEED_Y * self.vec[1]
            self.angle += CHANGE_ROT * self.rot_dir
            if self.angle > MAX_ROT:
                self.rot_dir = -1
            elif self.angle < MIN_ROT:
                self.rot_dir = 1
        else:
            self.angle = 0
            self.copy.change_x = 0
            self.copy.change_y = 0

    def set_position(self, center_x: float, center_y: float):
        self.copy.set_position(center_x, center_y)
        return super().set_position(center_x, center_y)

    def key_press(self, key: int, key_modifiers: int):
        """key_press
        Reacts to keys that are pressed that are fed down to this
        object
        """
        # pylint: disable=unused-argument
        move_x, move_y = self.vec
        if key == arcade.key.W:
            move_y = 1
        elif key == arcade.key.S:
            move_y = -1

        if key == arcade.key.A:
            move_x = -1
        elif key == arcade.key.D:
            move_x = 1
        self.vec = (move_x, move_y)
        self.moving = self.vec != (0, 0)

    def key_release(self, key: int, key_modifers: int):
        """key_press
        Reacts to keys that are released that are fed down to this
        object
        """
        # pylint: disable=unused-argument
        move_x, move_y = self.vec
        if key == arcade.key.W or key == arcade.key.S:
            move_y = 0
        if key == arcade.key.A or key == arcade.key.D:
            move_x = 0
        self.vec = (move_x, move_y)
        self.moving = self.vec != (0, 0)
