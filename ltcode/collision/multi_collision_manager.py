from collision.collision import is_collision_with_any_obstacle
from settings.settings import DISPLAY_WIDTH


class MultiCollisionManager:
    def __init__(self, player_list, obstacle_list):
        self.player_list = player_list
        self.obstacle_list = obstacle_list
        NUM_PLAYERS = len(player_list)
        self.x_shift = DISPLAY_WIDTH / NUM_PLAYERS

    def is_collision(self):
        '''Checks if any car collides with any object'''
        for player in self.player_list:
            x_car_shift = -(player.id * self.x_shift)
            if is_collision_with_any_obstacle(player.car, self.obstacle_list, x_car_shift):
                return True
        return False

    def current_crashing_players(self):
        '''Returns list of players that are crushing right now'''
        crashing_players = []
        for player in self.player_list:
            x_car_shift = -(player.id * self.x_shift)
            if is_collision_with_any_obstacle(player.car, self.obstacle_list, x_car_shift):
                crashing_players.append(player)
        return crashing_players