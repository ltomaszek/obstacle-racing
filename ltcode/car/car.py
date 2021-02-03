import pygame as pg
import random
from settings import settings

def get_starting_position(car_width, car_height):
    x = settings.DISPLAY_WIDTH / 2 - car_width / 2
    y = settings.DISPLAY_HEIGHT - car_height
    return (x, y)

class Car:

    def __init__(self, start_x, start_y, width, height, speed, img):
        self.start_x = start_x
        self.start_y = start_y
        self.widht = width
        self.height = height
        self.speed = speed
        self.img = img
        self.x_delta = 0

        self.reset()

    def move_left(self):
        self.x_delta = -self.speed

    def move_right(self):
        self.x_delta = self.speed

    def stop(self):
        self.x_delta = 0

    def update(self):
        self.x += self.x_delta

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def get_left_x(self):
        return self.x

    def get_right_x(self):
        return self.x + self.widht

    def get_front_y(self):
        return self.y

    def get_back_y(self):
        return self.y + self.height