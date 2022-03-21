import os

import arcade
import arcade.gui as gui

from ..player import Player
from .trevorscene import TrevorScene
from ..gui.bar import Bar

HEART_WIDTH=35
HEART_HEIGHT=35

class MainGameScene(arcade.Scene, TrevorScene):
    def __init__(self):
        super().__init__()

        self.player = Player()
        self.last_health = self.player.health
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.player)
        self.add_sprite_list("Player")
        self.add_sprite("Player", self.player)

        self.manager = None
        self.hbox = None
        self.heartfulltex = None
        self.heartemptytex = None
        self.heartwidgets = None
        self.__setup_gui()
        

    def __setup_gui(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        self.hbox = gui.UIBoxLayout(vertical=False)
        self.heartfulltex = arcade.Sprite(os.path.join("assets", "images", "heartfull.png"), 0.25)
        self.heartemptytex = arcade.Sprite(os.path.join("assets", "images", "heartempty.png"), 0.25)
        
        self.heartwidgets = []
        for i in range(Player.MAX_HEALTH):
            if i < self.player.health:
                widget = gui.UISpriteWidget(
                    x=i*HEART_WIDTH, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartfulltex
                )
                self.heartwidgets.append(widget.with_space_around(left=5, bottom=10))
            else:
                widget = gui.UISpriteWidget(
                    x=i*HEART_WIDTH, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartemptytex
                )
                self.heartwidgets.append(widget.with_space_around(left=5, bottom=10))
            self.hbox.add(self.heartwidgets[i])
        
        hydration_name = os.path.join("assets", "images", "hydration.png")
        # self.bar = Bar(hydration_name, 100, 0, 100, (255, 0, 0), (0, 255, 0), 150, 16, width=400)
        self.bar = Bar(
            texture_name=hydration_name,
            value=50,
            min_value=0,
            max_value=100,
            bg_color=(0, 0, 0),
            fill_color=(0, 0, 255),
            bar_width=150,
            bar_height=16,
            width=250
        )

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                align_x=10,
                child=self.hbox
            )
        )
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                align_x=10,
                align_y=HEART_HEIGHT,
                child=self.bar
            )
        )
    
    def draw(self):
        super().draw()
        self.manager.draw()
    
    def on_update(self, delta_time):
        self.player.update(delta_time)

        if self.player.health != self.last_health:
            diff = self.last_health - self.player.health
            sprite = self.heartemptytex if diff > 0 else self.heartfulltex

            if diff > 0:
                for i in range(self.player.health, self.last_health):
                    widget = gui.UISpriteWidget(
                        x=i*HEART_WIDTH, y=HEART_HEIGHT,
                        width=HEART_WIDTH, height=HEART_HEIGHT,
                        sprite=sprite
                    )
                    self.hbox.children[max(0,i)] = widget.with_space_around(left=5, bottom=10)
            else:
                for i in range(self.last_health, self.player.health):
                    widget = gui.UISpriteWidget(
                        x=i*HEART_WIDTH, y=HEART_HEIGHT,
                        width=HEART_WIDTH, height=HEART_HEIGHT,
                        sprite=sprite
                    )
                    self.hbox.children[min(Player.MAX_HEALTH-1,i)] = widget.with_space_around(left=5, bottom=10)
            self.last_health = self.player.health

    
    def on_key_press(self, key, key_modifiers):
        self.player.key_press(key, key_modifiers)

        if key == arcade.key.LEFT:
            self.player.health = max(0, self.player.health - 1)
        
        if key == arcade.key.RIGHT:
            self.player.health = min(self.player.health + 1, Player.MAX_HEALTH)
    
    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key, key_modifiers)
    
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass
    
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass