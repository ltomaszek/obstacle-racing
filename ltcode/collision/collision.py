from car.car import Car
from obstacle.obstacle import Obstacle

def is_collision_with_any_obstacle(car, obstacle_list) -> bool:
    for obstacle in obstacle_list:
        if is_collision(car, obstacle):
            return True
    return False

def is_collision(car, obstacle:Obstacle):
    return can_collide_Y(car, obstacle) and can_collide_X(car, obstacle)

def can_collide_Y(car:Car, obstacle:Obstacle):
    return car.get_front_y() <= obstacle.get_down_y() and car.get_back_y() >= obstacle.get_up_y()

def can_collide_X(car:Car, obstacle:Obstacle):
    return car.get_left_x() <= obstacle.get_right_x() and car.get_right_x() >= obstacle.get_left_x()
