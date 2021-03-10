import pygame as pg
import obstacle.obstacle as obstacle
from obstacle.obstacle import Obstacle
from settings import settings


class ObstacleManager:
    def __init__(self):
        self.obstacle_list = []

    def update(self, surface):
        # counts obstacle that hit the end of screen
        count_hit_end = 0
        for obstacle in self.obstacle_list:
            count_hit_end += obstacle.update()
        return count_hit_end

    def generate_random_obstacles(self, num_obstacles):
        for _ in range(num_obstacles):
            self.obstacle_list.append(Obstacle())

    def reset_all(self):
        for obstacle in self.obstacle_list:
            obstacle.reset()

    def level_up(self):
        self.obstacle_list.append(Obstacle())
        for obstacle in self.obstacle_list:
            obstacle.speed += 0.5

    def draw_all(self, surface):
        for obstacle in self.obstacle_list:
            self.draw(surface, obstacle)

    def draw(self, surface, obstacle, x_shift=0):
        pg.draw.rect(surface, obstacle.color, [obstacle.x + x_shift, obstacle.y, obstacle.width, obstacle.height])