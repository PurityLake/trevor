"""game.py
Contains the window class to which the game
draws and updates objects every frame.
"""

import arcade

from .scenes.trevorscene import TrevorScene
from .scenes.gamescene import MainGameScene

class Game(arcade.Window):
    """Game
    The window for the Trevor game. Mangages the window and uses
    scenes to decide what to draw and when
    """

    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.scene: TrevorScene
        self.setup()

    def setup(self):
        """setup
        Sets up the base objects for the game to be drawn and updated
        """
        self.scene = MainGameScene()

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.scene.on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.scene.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.scene.on_key_release(symbol, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.scene.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x: float, y: float, button, modifiers):
        self.scene.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.scene.on_mouse_release(x, y, button, modifiers)

    def set_mouse_platform_visible(self, platform_visible=None):
        pass
