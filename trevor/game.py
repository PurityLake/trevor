import arcade

from .scenes.trevorscene import TrevorScene
from .scenes.gamescene import MainGameScene

class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.scene: TrevorScene
        self.setup()

    def setup(self):
        self.scene = MainGameScene()

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.scene.on_update(delta_time)

    def on_key_press(self, key: int, key_modifiers: int):
        self.scene.on_key_press(key, key_modifiers)

    def on_key_release(self, key: int, key_modifiers: int):
        self.scene.on_key_release(key, key_modifiers)

    def on_mouse_motion(self, x: float, y: float, delta_x: float, delta_y: float):
        self.scene.on_mouse_motion(x, y, delta_x, delta_y)

    def on_mouse_press(self, x: float, y: float, button, key_modifiers):
        self.scene.on_mouse_press(x, y, button, key_modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, key_modifiers: int):
        self.scene.on_mouse_release(x, y, button, key_modifiers)