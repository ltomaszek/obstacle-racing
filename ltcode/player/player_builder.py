import pygame as pg
from player.player import Player
from settings.settings import DISPLAY_WIDTH
from settings import car
from settings.player import LIVES, KEYS, KEY_LEFT, KEY_RIGHT
from car.car import Car


class PlayerBuilder:
    def __init__(self, num_players=1):
        self.NUM_PLAYERS = num_players

    def get_players(self):
        car_img = pg.image.load('graphics/car.png')
        player_list = []

        for i in range(self.NUM_PLAYERS):
            x_min = i * DISPLAY_WIDTH / self.NUM_PLAYERS
            x_max = (i + 1) * DISPLAY_WIDTH / self.NUM_PLAYERS - 1 # -1 cause its inclusive and we want it exclusive
            car = Car(x_min, x_max, 8, car_img)
            player = Player(i, LIVES, car, KEYS[i]['left'], KEYS[i]['right'])
            player_list.append(player)
        return player_list

    def get_player(self):
        car_img = pg.image.load('graphics/car.png')
        car = Car(0, DISPLAY_WIDTH, 8, car_img)
        return Player(0, 3, car, KEY_LEFT, KEY_RIGHT)

