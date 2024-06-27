"""
name: Pytruck
author: Igor Vasiljev

email: va1ngvarr@outlook.com
repo: https://github.com/va1ngvarr/Pytruck

"""

import sys

import pygame
from pygame.locals import *

from Car import BotCar, PlayerCar, BaseCar
from settings import WIDTH, HEIGHT, FPS, BOTS_AMOUNT

# INITIALIZATION AND PARAMETERS
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

TargetFPS = pygame.time.Clock().tick


def tick_and_process_events(cars: list[BaseCar]) -> None:
    TargetFPS(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        for car in cars:
            car.on_pygame_event(event)


def draw_loop(cars: list[BaseCar]) -> None:
    for car in cars:
        screen.blit(car.car, car.car_rect)


def update_loop(cars: list[BaseCar]) -> None:
    for car in cars:
        car.update()


def draw_background():
    screen.fill((255, 255, 255))


def mainloop(cars: list[BaseCar]) -> None:
    while True:
        tick_and_process_events(cars)

        draw_background()

        draw_loop(cars)
        update_loop(cars)

        pygame.display.update()


def main():
    cars = [PlayerCar()]
    cars.extend([BotCar() for _ in range(BOT_AMOUNT)])

    mainloop(cars)


if __name__ == "__main__":
    main()
