import arcade

MIN_ROT = -25
MAX_ROT = 25
CHANGE_ROT = 3.5
FILENAME = "assets/images/steve.png"
SPEED_X = 5
SPEED_Y = 5


class Player(arcade.Sprite):
    MAX_HEALTH = 5

    def __init__(self):
        super().__init__(FILENAME, 1)

        self.moving = False
        self.vec = (0, 0)
        self.rot_dir = 1
        self.set_position(100, 100)

        self.health = 5
    
    def update(self, delta_time):
        if self.moving:
            self.set_position(
                self.center_x + SPEED_X * self.vec[0],
                self.center_y + SPEED_Y * self.vec[1])
            self.angle += CHANGE_ROT * self.rot_dir
            if self.angle > MAX_ROT:
                self.rot_dir = -1
            elif self.angle < MIN_ROT:
                self.rot_dir = 1
        else:
            self.angle = 0
    
    def key_press(self, key):
        move_x, move_y = self.vec
        if key == arcade.key.W:
            move_y = 1
        elif key == arcade.key.S:
            move_y = -1
        
        if key == arcade.key.A:
            move_x = -1
        elif key == arcade.key.D:
            move_x = 1
        self.vec = (move_x, move_y)
        self.moving = self.vec != (0, 0)
    
    def key_release(self, key):
        move_x, move_y = self.vec
        if key == arcade.key.W or key == arcade.key.S:
            move_y = 0
        if key == arcade.key.A or key == arcade.key.D:
            move_x = 0
        self.vec = (move_x, move_y)
        self.moving = self.vec != (0, 0)