"""trevorscene.py
Defines thhe abstract base class TrevorScene
"""

from abc import ABC, abstractmethod

# pylint: disable=invalid-name

class TrevorScene(ABC):
    """TrevorScene
    Abstract base class that all scenes in this game must implement
    """

    @abstractmethod
    def on_update(self, delta_time: float):
        """on_update
        Called every tick to update the scene internals
        """

    @abstractmethod
    def on_key_press(self, key: int, key_modifiers: int):
        """on_key_press
        Called every time a key is pressed
        """

    @abstractmethod
    def on_key_release(self, key: int, key_modifiers: int):
        """on_key_release
        Called every time a key is released
        """

    @abstractmethod
    def on_mouse_motion(self, x: float, y: float, delta_x: float, delta_y: float):
        """on_mouse_motions
        Called every time the mouse moves
        """

    @abstractmethod
    def on_mouse_press(self, x: float, y: float, button: int, key_modifiers: int):
        """on_mouse_press
        Called every time a mouse button is pressed
        """

    @abstractmethod
    def on_mouse_release(self, x: float, y: float, button: int, key_modifiers: int):
        """on_mouse_release
        Called every time a mouse button is released
        """
