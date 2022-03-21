from turtle import fillcolor
import arcade
import arcade.gui as gui
from arcade.experimental.uislider import UISlider
from arcade.experimental.uistyle import UISliderStyle

class Bar(gui.UIWidget):
    def __init__(self,
        texture_name,
        value,
        min_value,
        max_value,
        bg_color,
        fill_color,
        bar_width,
        bar_height,
        x=0,
        y=0,
        width=100,
        height=100,
        children=[],
        size_hint=None,
        size_hint_min=None,
        size_hint_max=None,
        style=None,
        **kwargs
        ):
        super().__init__(x, y, width, height, children, size_hint, size_hint_min, size_hint_max, style, **kwargs)
        self.texture = arcade.load_texture(texture_name)
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.bg_color = bg_color
        self.fill_color = fill_color
        self.bar_width = bar_width
        self.bar_height = bar_height
    
    def do_render(self, surface):
        self.prepare_render(surface)
        arcade.draw_texture_rectangle(self.x+5, self.y, 32, 32, self.texture)
        arcade.draw_xywh_rectangle_filled(self.x+30, self.y-self.bar_height/2, self.bar_width, self.bar_height, self.bg_color)
        arcade.draw_xywh_rectangle_filled(self.x+30, self.y-self.bar_height/2, self.bar_width * (self.value / self.max_value), self.bar_height, self.fill_color)

