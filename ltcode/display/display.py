import pygame as pg
import time
from settings import color
from settings.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT


class Display:
    def __init__(self, game_display):
        self.game_display = game_display

    def update(self):
        pg.display.update()

    # Display text on screen
    def message_display(self, text, font, coor_side, coor):
        text_surface, text_rectangle = self.text_objects(text, font, color.BLACK)
        if coor_side == 'center':
            text_rectangle.center = coor
        elif coor_side == 'left':
            text_rectangle.topleft = coor
        self.game_display.blit(text_surface, text_rectangle)

    def clear(self):
        self.game_display.fill(color.WHITE)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def draw_crash(self):
        font = pg.font.Font('freesansbold.ttf', 115)
        coor = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.message_display("You Crashed", font, 'center', coor)
        self.update()
        time.sleep(1)

    def draw_game_over(self):
        font = pg.font.Font('freesansbold.ttf', 115)
        coor = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.clear()
        self.message_display("GAME OVER", font, 'center', coor)
        self.update()
        time.sleep(1)

    def draw_score(self, score):
        font = pg.font.Font('freesansbold.ttf', 24)
        coor = (30, 30)
        self.message_display(f"Score: {score}", font, 'left', coor)

    def draw_lives(self, lives):
        font = pg.font.Font('freesansbold.ttf', 24)
        coor = (30, 10)
        self.message_display(f"Lives: {lives}", font, 'left', coor)

    def draw_level(self, level):
        font = pg.font.Font('freesansbold.ttf', 115)
        coor = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.message_display(f"Level {level}", font, 'center', coor)
        self.update()
        time.sleep(1)