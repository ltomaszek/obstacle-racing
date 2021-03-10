import pygame as pg
from settings.settings import DISPLAY_WIDTH
from settings import car
from settings.player import LIVES, KEYS, KEY_LEFT, KEY_RIGHT
from car.car import Car


class Player:
    def __init__(self, id, lives, car, left_key, right_key):
        self.id = id
        self.lives = lives
        self.car = car
        self.left_key = left_key
        self.right_key = right_key

    def update_key(self, pressed_keys):
        if pressed_keys[self.left_key]:
            self.car.move_left()
        elif pressed_keys[self.right_key]:
            self.car.move_right()
        else:
            self.car.stop()

    def update(self):
        self.car.update()

    def level_up(self):
        self.car.speed += 0.5

    def draw(self, surface):
        self.car.draw(surface)

    def reset(self):
        self.car.reset()

    def is_alive(self):
        return self.lives > 0


