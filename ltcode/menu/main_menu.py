import pygame as pg
from settings import color
from settings import car
from settings import settings
import time

car_img = pg.image.load('graphics/car.png')
arrow_img = pg.image.load('graphics/arrow.png')

class MainMenu:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pg.time.Clock()


    def start(self):
        '''Returns number of player'''
        self.show_cars()
        self.show_options_menu()

        pg.display.update()
        cursor = Cursor(self.surface)
        cursor.draw()

        enter_pressed = False
        while not enter_pressed:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        cursor.up()
                    elif event.key == pg.K_DOWN:
                        cursor.down()
                    elif event.key == pg.K_RETURN:
                        enter_pressed = True

        return cursor.position;

    def show_cars(self):
        curr_x = - car.CAR_WIDTH
        end_x = settings.DISPLAY_WIDTH / 3
        car_speed = 8
        car_y = settings.DISPLAY_HEIGHT - 20 - car.CAR_HEIGHT
        while curr_x < end_x:
            self.surface.fill(color.WHITE)
            curr_x += car_speed
            self.surface.blit(car_img, (curr_x, car_y))
            self.surface.blit(car_img, (settings.DISPLAY_WIDTH - curr_x - car.CAR_WIDTH, car_y))
            pg.display.update()
            self.clock.tick(settings.FPS)

    def show_options_menu(self):
        self.number_players()

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, text, font, coor_side, coor):
        text_surface, text_rectangle = self.text_objects(text, font, color.BLACK)
        if coor_side == 'center':
            text_rectangle.center = coor
        elif coor_side == 'left':
            text_rectangle.topleft = coor
        self.surface.blit(text_surface, text_rectangle)

    def number_players(self):
        font = pg.font.Font('freesansbold.ttf', 80)
        x = settings.DISPLAY_WIDTH / 2
        y = settings.DISPLAY_HEIGHT / 4
        self.message_display("Players:", font, 'center', (x, y))
        for player_idx in range(4):
            self.message_display(f'{player_idx + 1}', font, 'center', (x, y + (player_idx+1) * 100))


class Cursor:
    def __init__(self, surface):
        self.position = 1
        self.x = settings.DISPLAY_WIDTH / 2 - 150
        self.start_y = settings.DISPLAY_HEIGHT / 4 - 50
        self.surface = surface

    def get_y(self):
        return self.start_y + self.position * 100

    def draw(self):
        self.surface.blit(arrow_img, (self.x, self.get_y()))
        pg.display.update()

    def up(self):
        self.surface.fill(color.WHITE, [self.x, self.get_y(), 100, 100])
        if self.position == 1:
            self.position = 4
        else:
            self.position -= 1
        self.draw()

    def down(self):
        self.surface.fill(color.WHITE, [self.x, self.get_y(), 100, 100])
        if self.position == 4:
            self.position = 1
        else:
            self.position += 1
        self.draw()