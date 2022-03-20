import arcade
import arcade.gui as gui

from .player import Player

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.player = None
        self.wood_sprite = None
        self.sword_sprite = None
        self.sprite_list = None
        self.setup()

    def setup(self):
        self.sprite_list = arcade.SpriteList()
        self.player = Player()
        self.wood_sprite = arcade.Sprite("assets/images/wood.png", 1.5)
        self.wood_sprite.position = (100, 100)
        self.sword_sprite = arcade.Sprite("assets/images/ironsword.png", 1.5)
        self.sword_sprite.position = (200, 100)
        
        self.sprite_list.append(self.player)
        # self.sprite_list.append(self.wood_sprite)
        # self.sprite_list.append(self.sword_sprite)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()

    def on_update(self, delta_time):
        self.player.update(delta_time)
        self.sword_sprite.angle = (self.sword_sprite.angle + 5) % 360

    def on_key_press(self, key, key_modifiers):
        self.player.key_press(key)

    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass