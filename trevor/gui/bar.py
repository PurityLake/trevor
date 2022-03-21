"""bar.py
Contains the Bar class
"""
# pylint: disable=disallowed-name
from typing import Tuple, Iterable

import arcade
import arcade.gui as gui

class Bar(gui.UIWidget):
    """Bar
    This class is a custom widget that implements
    a fillable bar that is used to represent
    a percentage of a value compared to a max value
    """

    def __init__(self,
        texture_name: str,
        value: int,
        min_value: int,
        max_value: int,
        bg_color: Tuple[int, int, int],
        fill_color: Tuple[int, int, int],
        bar_width: int,
        bar_height:  int,
        x: float = 0,
        y: float = 0,
        width: float = 100,
        height: float = 100,
        children: Iterable[gui.UIWidget] = [],
        size_hint=None,
        size_hint_min=None,
        size_hint_max=None,
        style=None,
        **kwargs
        ):
        # pylint: disable=dangerous-default-value
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            children=children,
            size_hint=size_hint,
            size_hint_min=size_hint_min,
            size_hint_max=size_hint_max,
            style=style,
            **kwargs)
        self.texture: arcade.Texture = arcade.load_texture(texture_name)
        self.value: int = value
        self.min_value: int = min_value
        self.max_value: int = max_value
        self.bg_color: Tuple[int, int, int] = bg_color
        self.fill_color: Tuple[int, int, int] = fill_color
        self.bar_width: int = bar_width
        self.bar_height: int = bar_height

    def do_render(self, surface: gui.Surface):
        self.prepare_render(surface)
        arcade.draw_texture_rectangle(self.x+5, self.y, 32, 32, self.texture)
        arcade.draw_xywh_rectangle_filled(
            self.x+30,
            self.y-self.bar_height/2,
            self.bar_width,
            self.bar_height,
            self.bg_color)
        arcade.draw_xywh_rectangle_filled(
            self.x+30,
            self.y-self.bar_height/2,
            self.bar_width * (self.value / self.max_value),
            self.bar_height,
            self.fill_color)
