import pygame as pg
import random
from settings.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT
from settings.obstacle import *
from settings.color import *

class Obstacle:

    # for each -1 value, a new random value will be generated
    def __init__(self, x=-1, y=-1, width=-1, height=-1, speed=-1, color=-1):
        self.width = self.get_random_width() if width == -1 else x
        self.height = self.get_random_height() if height == -1 else x
        self.x = self.get_random_x() if x == -1 else x
        self.y = self.get_random_y() if y == -1 else x
        self.speed = random.randint(MIN_SPEED, MAX_SPEED) if speed == -1 else speed
        self.color = self.get_random_color() if color == -1 else color

    # returns True if it reached the end of down screen and needs to start over
    def update(self):
        self.y += self.speed
        if self.y > DISPLAY_HEIGHT:
            self.reset()
            return True
        return False

    def reset(self):
        self.widht = self.get_random_width()
        self.height = self.get_random_height()
        self.x = self.get_random_x()
        self.y = self.get_random_y()

    def get_random_width(self):
        return random.randint(MIN_WIDTH, MAX_WIDTH)

    def get_random_height(self):
        return random.randint(MIN_HEIGHT, MAX_HEIGHT)

    def get_random_x(self):
        return random.randint(0, DISPLAY_WIDTH - self.width)

    def get_random_y(self):
        return -self.height - random.randint(0, 1000)

    def get_random_color(self):
        min = 50
        max = 255
        return (random.randint(min, max), random.randint(min, max), random.randint(min, max))

    def draw(self, surface):
        pg.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])

    def get_left_x(self):
        return self.x

    def get_right_x(self):
        return self.x + self.width

    def get_up_y(self):
        return self.y

    def get_down_y(self):
        return self.y + self.height
