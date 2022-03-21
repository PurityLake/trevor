import os
from typing import List, Optional

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

        self.tile_map = arcade.load_tilemap(os.path.join("assets", "maps", "trevorexamplemap.tmx"))
        self.end_of_map = self.tile_map.width
        self.tile_map_sprite_list = arcade.SpriteList()
        self.tile_map.scaling = 1

        self.add_sprite_list("Map", True, self.tile_map.sprite_lists["Map"])
        self.add_sprite_list("Plants", sprite_list=self.tile_map.sprite_lists["Plants"])

        self.player: Player = Player()
        self.last_health: int = self.player.health
        self.sprite_list: arcade.SpriteList = arcade.SpriteList()
        self.sprite_list.append(self.player)
        self.add_sprite_list("Player")
        self.add_sprite("Player", self.player)

        self.manager: gui.UIManager = None
        self.hbox: gui.UIBoxLayout = None
        self.heartfullsprite: arcade.Sprite = None
        self.heartemptysprite: arcade.Sprite = None
        self.heartwidgets: List[gui.UISpriteWidget] = None
        self.__setup_gui()
        

    def __setup_gui(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        self.hbox = gui.UIBoxLayout(vertical=False)
        self.heartfullsprite = arcade.Sprite(os.path.join("assets", "images", "heartfull.png"), 0.25)
        self.heartemptysprite = arcade.Sprite(os.path.join("assets", "images", "heartempty.png"), 0.25)
        
        self.heartwidgets = []
        for i in range(Player.MAX_HEALTH):
            if i < self.player.health:
                widget = gui.UISpriteWidget(
                    x=i*HEART_WIDTH, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartfullsprite
                )
                self.heartwidgets.append(widget.with_space_around(left=5, bottom=10))
            else:
                widget = gui.UISpriteWidget(
                    x=i*HEART_WIDTH, y=HEART_HEIGHT,
                    width=HEART_WIDTH, height=HEART_HEIGHT,
                    sprite=self.heartemptysprite
                )
                self.heartwidgets.append(widget.with_space_around(left=5, bottom=10))
            self.hbox.add(self.heartwidgets[i])
        
        hydration_name = os.path.join("assets", "images", "hydration.png")
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


    def on_update(self, delta_time: float = 1 / 60, names: Optional[List[str]] = None):
        self.player.on_update(delta_time)

        if self.player.health != self.last_health:
            diff = self.last_health - self.player.health
            sprite = self.heartemptysprite if diff > 0 else self.heartfullsprite

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

    
    def on_key_press(self, key: int, key_modifiers: int):
        self.player.key_press(key, key_modifiers)

        if key == arcade.key.LEFT:
            self.player.health = max(0, self.player.health - 1)
        
        if key == arcade.key.RIGHT:
            self.player.health = min(self.player.health + 1, Player.MAX_HEALTH)
    
    def on_key_release(self, key, key_modifiers):
        self.player.key_release(key, key_modifiers)
    
    def on_mouse_motion(self, x: float, y: float, delta_x: float, delta_y: float):
        pass
    
    def on_mouse_press(self, x: float, y: float, button: int, key_modifiers: int):
        pass
    
    def on_mouse_release(self, x: float, y: float, button: int, key_modifiers: int):
        pass