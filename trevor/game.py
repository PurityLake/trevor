import arcade
import arcade.gui as gui

from .scenes.gamescene import MainGameScene

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.scene = None
        self.setup()

    def setup(self):
        self.scene = MainGameScene()

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
        self.scene.on_update(delta_time)

    def on_key_press(self, key, key_modifiers):
        self.scene.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.scene.on_key_release(key, key_modifiers)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.scene.on_mouse_motion(x, y, delta_x, delta_y)

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.scene.on_mouse_press(x, y, button, key_modifiers)

    def on_mouse_release(self, x, y, button, key_modifiers):
        self.scene.on_mouse_release(x, y, button, key_modifiers)