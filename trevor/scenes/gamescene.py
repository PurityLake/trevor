import os

import arcade
import arcade.gui as gui

from ..player import Player
from .trevorscene import TrevorScene

HEART_WIDTH=35
HEART_HEIGHT=35

class MainGameScene(arcade.Scene, TrevorScene):
    def __init__(self):
        super().__init__()

        self.player = Player()
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.player)
        self.add_sprite_list(self.sprite_list)

        self.manager = gui.UIManager()
        self.manager.enable()

        self.hbox = gui.UIBoxLayout(vertical=False)
        self.heartfulltex = arcade.Sprite(os.path.join("assets", "images", "heartfull.png"), 0.25)
        self.heartemptytex = arcade.Sprite(os.path.join("assets", "images", "heartempty.png"), 0.25)
        
        self.heartwidgets = []
        for i in range(Player.MAX_HEALTH):
            if i < self.player.health:
                widget = gui.UISpriteWidget(
                    x=20+i*64, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartfulltex
                )
                self.heartwidgets.append(widget.with_space_around(right=5, bottom=10))
            else:
                widget = widget = gui.UISpriteWidget(
                    x=20+i*64, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartemptytex
                )
                self.heartwidgets.append(widget.with_space_around(right=5, bottom=10))
            self.hbox.add(self.heartwidgets[i])
        
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                child=self.hbox
            )
        )
    
    def draw(self):
        super().draw()
        self.manager.draw()
    
    def on_update(self, delta_time):
        self.player.update(delta_time)
    
    def on_key_press(self, key, key_modifiers):
        self.player.key_press(key, key_modifiers)
    
    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key, key_modifiers)
    
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass
    
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass