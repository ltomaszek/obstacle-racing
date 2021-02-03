import pygame as pg
from car.car import *
from collision.collision import is_collision_with_any_obstacle
from settings import settings
from obstacle.obstacle_manager import ObstacleManager
from display.display import Display
import graphics as g

FPS = 60    # frame per seconds
pg.init()

display_width = settings.DISPLAY_WIDTH
display_height = settings.DISPLAY_HEIGHT

game_display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Race Car')
display = Display(game_display)

clock = pg.time.Clock()

car_img_width = 66
car_img_height = 142
car_img = pg.image.load('graphics/car.png')

start_x, start_y = get_starting_position(car_img_width, car_img_height)

car = Car(start_x, start_y, car_img_width, car_img_height, 8, car_img)


def game_loop():
    NUM_OBSTACLES = 4
    obstacle_manager = ObstacleManager()
    obstacle_manager.generate_random_obstacles(NUM_OBSTACLES)

    lives = 3
    level = 1
    target_score = 10

    while lives > 0:
        display.clear()
        display.draw_level(level)
        is_next_level = round_start(lives, target_score, obstacle_manager)

        if is_next_level:
            level += 1
            car.speed += 0.5
            obstacle_manager.level_up()
        else:
            lives -= 1
            display.draw_crash()

    display.draw_game_over()


def round_start(lives, target_score, obstacle_manager):
    '''Returns True if target_score has been reach or False if collision happened'''
    car.reset()
    obstacle_manager.reset_all()

    is_collision = False
    round_score = 0

    while not is_collision and round_score < target_score:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            pressed_keys = pg.key.get_pressed()

            if pressed_keys[pg.K_LEFT]:
                car.move_left()
            elif pressed_keys[pg.K_RIGHT]:
                car.move_right()
            else:
                car.stop()

        display.clear()

        car.update()
        car.draw(game_display)

        # update coordinates and draw obstacles
        round_score += obstacle_manager.update_all(game_display)

        display.draw_score(round_score)
        display.draw_lives(lives)

        display.update()

        # collisions with wall
        collision_with_wall = car.x < 0 or car.x + car_img_width > display_width
        collision_with_obstacle = is_collision_with_any_obstacle(car, obstacle_manager.obstacle_list)

        if(collision_with_wall or collision_with_obstacle):
            is_collision = True

        # pg.display.update(xxx) - updates a specific object
        # pg.display.update() - updates entire surface
        # pg.display.flip() - updates entire surface

        clock.tick(FPS)

    if is_collision:
        return False
    else:
        return True


game_loop()
