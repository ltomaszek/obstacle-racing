import pygame as pg
from settings import color
from settings.settings import DISPLAY_WIDTH, DISPLAY_HEIGHT


class MultiDisplay:
    def __init__(self, game_display, player_list):
        self.game_display = game_display
        self.player_list = player_list
        self.PLAYER_DISPLAY_WIDTH = DISPLAY_WIDTH / len(player_list)

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

    def draw_crash(self, crashed_players):
        font = pg.font.Font('freesansbold.ttf', 45)
        for player in crashed_players:
            coor = (self.PLAYER_DISPLAY_WIDTH / 2 + (player.id * self.PLAYER_DISPLAY_WIDTH), DISPLAY_HEIGHT / 2)
            self.message_display("You Crashed", font, 'center', coor)
        self.update()

    def draw_game_over(self, player):
        font = pg.font.Font('freesansbold.ttf', 60)
        coor = (self.PLAYER_DISPLAY_WIDTH / 2 + (player.id * self.PLAYER_DISPLAY_WIDTH), DISPLAY_HEIGHT / 2)
        self.message_display("GAME OVER", font, 'center', coor)
        self.update()

    def draw_score(self, player):
        font = pg.font.Font('freesansbold.ttf', 24)
        coor = (30, 30)
        self.message_display(f"Score: {player.score}", font, 'left', coor)

    def draw_lives(self):
        font = pg.font.Font('freesansbold.ttf', 24)
        for player in self.player_list:
            coor = (30 + (player.id * self.PLAYER_DISPLAY_WIDTH), 10)
            self.message_display(f"Lives: {player.lives}", font, 'left', coor)

    def draw_level(self, level):
        font = pg.font.Font('freesansbold.ttf', 115)
        coor = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.message_display(f"Level {level}", font, 'center', coor)
        self.update()

    def draw_winner(self, player):
        font = pg.font.Font('freesansbold.ttf', 60)
        coor = (self.PLAYER_DISPLAY_WIDTH / 2 + (player.id * self.PLAYER_DISPLAY_WIDTH), DISPLAY_HEIGHT / 2)
        self.clear()
        self.message_display("WINNER", font, 'center', coor)
        self.update()

    def draw_no_winner(self):
        font = pg.font.Font('freesansbold.ttf', 155)
        coor = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.clear()
        self.message_display("NO WINNER", font, 'center', coor)
        self.update()