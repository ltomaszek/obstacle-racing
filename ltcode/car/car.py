import pygame as pg
import random
from settings import settings
from settings.car import CAR_WIDTH, CAR_HEIGHT


def get_starting_position(min_x, max_x):
    range = max_x - min_x
    x = min_x + range / 2 - CAR_WIDTH / 2
    y = settings.DISPLAY_HEIGHT - CAR_HEIGHT
    return (x, y)


class Car:
    def __init__(self, x_min, x_max, speed, img):
        self.x_min = x_min
        self.x_max = x_max
        self.speed = speed
        self.img = img
        self.x = None
        self.y = None
        self.reset();
        self.x_delta = 0

        self.reset()

    def move_left(self):
        self.x_delta = -self.speed

    def move_right(self):
        self.x_delta = self.speed

    def stop(self):
        self.x_delta = 0

    def update(self):
        if self.x_delta == 0:
            return
        if self.x_delta > 0:
            self.x = min(self.x_max - CAR_WIDTH, self.x + self.x_delta)
        else:
            self.x = max(self.x_min, self.x + self.x_delta)

    def reset(self):
        self.x, self.y = get_starting_position(self.x_min, self.x_max)

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def get_left_x(self):
        return self.x

    def get_right_x(self):
        return self.x + CAR_WIDTH

    def get_front_y(self):
        return self.y

    def get_back_y(self):
        return self.y + CAR_HEIGHT