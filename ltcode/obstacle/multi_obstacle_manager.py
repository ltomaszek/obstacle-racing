from obstacle.obstacle_manager import ObstacleManager
from settings.settings import DISPLAY_WIDTH
from obstacle import obstacle


class MultiObstacleManager(ObstacleManager):
    def __init__(self, player_list):
        super().__init__()
        self.player_list = player_list
        NUM_PLAYERS = len(player_list)
        self.X_SHIFT = DISPLAY_WIDTH / NUM_PLAYERS

        obstacle.MAX_X /= NUM_PLAYERS

    def update_all(self, surface):
        # update for 1st player like in single-player mode
        count_hit_end = super().update(surface)

        # draw obstacles for the rest of the alive players
        for player in self.player_list:
            if not player.is_alive():
                continue

            for obstacle in self.obstacle_list:
                self.draw(surface, obstacle, self.X_SHIFT * player.id)

        return count_hit_end