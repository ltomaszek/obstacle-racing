from obstacle.obstacle import Obstacle

class ObstacleManager:

    def __init__(self, obstacle_list=[]):
        self.obstacle_list = obstacle_list

    def update_all(self, surface):
        # counts obstacle that hit the end of screen
        count_hit_end = 0
        for obstacle in self.obstacle_list:
            count_hit_end += obstacle.update()
            obstacle.draw(surface)
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