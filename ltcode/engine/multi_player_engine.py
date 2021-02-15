import pygame as pg
import time
from car.car import *
from collision.collision import is_collision_with_any_obstacle
from collision.multi_collision_manager import MultiCollisionManager
from settings import settings
from settings import car
from player.player import Player
from player.player_builder import PlayerBuilder
from player.players_manager import PlayersManager
from obstacle.multi_obstacle_manager import MultiObstacleManager
from display.multi_display import MultiDisplay
import graphics as g


class MultiPlayerEngine:
    def __init__(self, NUM_PLAYERS):
        self.NUM_PLAYERS = NUM_PLAYERS
        self.game_display = pg.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
        self.clock = pg.time.Clock()

        player_list = PlayerBuilder(self.NUM_PLAYERS).get_players()
        self.players_manager = PlayersManager(player_list)

        self.display = MultiDisplay(self.game_display, player_list)

        NUM_OBSTACLES = 4
        self.obstacle_manager = MultiObstacleManager(player_list)
        self.obstacle_manager.generate_random_obstacles(NUM_OBSTACLES)

        self.collision_manager = MultiCollisionManager(player_list, self.obstacle_manager.obstacle_list)

        self.target_score = 10

    def game_loop(self):
        level = 1
        target_score = 10

        # continue when more than one player has at least one more live
        while self.players_manager.number_alive() > 1:
            self.display.clear()
            self.display.draw_level(level)
            time.sleep(1)

            crashed_players = self.round_start()

            # Go to next round if no players crashed
            if crashed_players == None:
                level += 1
                self.players_manager.level_up()
                self.obstacle_manager.level_up()
            else:
                self.players_manager.decrease_live(crashed_players)
                self.display.draw_crash(crashed_players)
                time.sleep(1)

                # game over for some player
                self.display.clear()
                for player in crashed_players:
                    if not player.is_alive():
                        self.display.draw_game_over(player)
                time.sleep(1)

        if self.players_manager.is_winner():
            winner = self.players_manager.get_winner()
            self.display.draw_winner(winner)
        else:
            self.display.draw_no_winner()
        time.sleep(3)

    def round_start(self):
        '''Returns True if target_score has been reach or False if collision happened'''
        self.players_manager.reset_players()
        self.obstacle_manager.reset_all()

        is_collision = False
        round_score = 0

        while not is_collision and round_score < self.target_score:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                # update players depending on pressed keys
                self.players_manager.update_players_key(pg.key.get_pressed())

            self.players_manager.update_players()

            self.display.clear()
            self.players_manager.draw_players(self.game_display)

            # update coordinates and draw obstacles
            round_score += self.obstacle_manager.update_all(self.game_display)

            #self.display.draw_score(round_score)
            self.display.draw_lives()

            self.display.update()

            is_collision = self.collision_manager.is_collision()

            self.clock.tick(settings.FPS)

        if is_collision:
            return self.collision_manager.current_crashing_players()
        else:
            return None