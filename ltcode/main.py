import pygame as pg
from menu.main_menu import MainMenu
from settings import settings
from engine.single_player_engine import SinglePlayerEngine
from engine.multi_player_engine import MultiPlayerEngine

import pygame as pg
from car.car import *
from collision.collision import is_collision_with_any_obstacle

pg.init()
pg.display.set_caption('Race Car')

surface = pg.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))


main_menu = MainMenu(surface)
NUM_PLAYERS = main_menu.start()

if NUM_PLAYERS == 1:
    SinglePlayerEngine(surface).game_loop()
else:
    MultiPlayerEngine(surface, NUM_PLAYERS).game_loop()

