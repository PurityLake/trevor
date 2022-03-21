from abc import ABC, abstractmethod

class TrevorScene(ABC):
    @abstractmethod
    def on_update(self, delta_time):
        pass

    @abstractmethod
    def on_key_press(self, key, key_modifiers):
        pass

    @abstractmethod
    def on_key_release(self, key, key_modifiers):
        pass

    @abstractmethod
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    @abstractmethod
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    @abstractmethod
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass