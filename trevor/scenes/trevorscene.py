from abc import ABC, abstractmethod

class TrevorScene(ABC):
    @abstractmethod
    def on_update(self, delta_time: float):
        pass

    @abstractmethod
    def on_key_press(self, key: int, key_modifiers: int):
        pass

    @abstractmethod
    def on_key_release(self, key: int, key_modifiers: int):
        pass

    @abstractmethod
    def on_mouse_motion(self, x: float, y: float, delta_x: float, delta_y: float):
        pass

    @abstractmethod
    def on_mouse_press(self, x: float, y: float, button: int, key_modifiers: int):
        pass

    @abstractmethod
    def on_mouse_release(self, x: float, y: float, button: int, key_modifiers: int):
        pass