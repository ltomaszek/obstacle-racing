import pygame as pg
from car.car import *
from collision.collision import is_collision_with_any_obstacle
from settings import settings
from obstacle.obstacle_manager import ObstacleManager
from display.display import Display
from player.player import Player
from player.player_builder import PlayerBuilder
import graphics as g


class SinglePlayerEngine:
    def __init__(self, surface):
        self.surface = surface
        self.display = Display(self.surface)

        self.clock = pg.time.Clock()

        self.car_img_width = 66
        self.car_img_height = 142

        self.player = PlayerBuilder().get_player()

    def game_loop(self):
        NUM_OBSTACLES = 4
        obstacle_manager = ObstacleManager()
        obstacle_manager.generate_random_obstacles(NUM_OBSTACLES)

        level = 1
        target_score = 10

        while self.player.lives > 0:
            self.display.clear()
            self.display.draw_level(level)
            is_next_level = self.round_start(target_score, obstacle_manager)

            if is_next_level:
                level += 1
                self.player.level_up()
                obstacle_manager.level_up()
            else:
                self.player.lives -= 1
                self.display.draw_crash()

        self.display.draw_game_over()

    def round_start(self, target_score, obstacle_manager):
        '''Returns True if target_score has been reach or False if collision happened'''
        self.player.reset()
        obstacle_manager.reset_all()

        is_collision = False
        round_score = 0

        while not is_collision and round_score < target_score:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                pressed_keys = pg.key.get_pressed()
                self.player.update_key(pressed_keys)

            self.display.clear()

            self.player.update()
            # update coordinates and draw obstacles
            round_score += obstacle_manager.update(self.surface)
            obstacle_manager.draw_all(self.surface)

            self.player.draw(self.surface)
            self.display.draw_score(round_score)
            self.display.draw_lives(self.player.lives)
            self.display.update()

            is_collision = is_collision_with_any_obstacle(self.player.car, obstacle_manager.obstacle_list)

            # pg.display.update(xxx) - updates a specific object
            # pg.display.update() - updates entire surface
            # pg.display.flip() - updates entire surface

            self.clock.tick(settings.FPS)

        if is_collision:
            return False
        else:
            return True