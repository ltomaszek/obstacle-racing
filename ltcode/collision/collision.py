from car.car import Car
from obstacle.obstacle import Obstacle


def is_collision_with_any_obstacle(car, obstacle_list, x_car_shift=0) -> bool:
    for obstacle in obstacle_list:
        if is_collision(car, obstacle, x_car_shift):
            return True
    return False


def is_collision(car, obstacle:Obstacle, x_car_shift):
    return _can_collide_Y(car, obstacle) and _can_collide_X(car, obstacle, x_car_shift)


def _can_collide_Y(car:Car, obstacle:Obstacle):
    return car.get_front_y() <= obstacle.get_down_y() and car.get_back_y() >= obstacle.get_up_y()


def _can_collide_X(car:Car, obstacle:Obstacle, x_car_shift):
    return car.get_left_x() + x_car_shift <= obstacle.get_right_x() \
           and car.get_right_x() + x_car_shift >= obstacle.get_left_x()