import pygame

from . import Car
from settings import WIDTH, HEIGHT

class Player(Car):
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.degree = 0

        Car.create(self, 'Sprites//car_player.png')
        self.car_rect = self.car.get_rect(center=(self.x, self.y))
        self.car_clean = self.car.copy()

    def bindings(self, i):
        # ROTATION RIGHT AND LEFT / FORWARD AND BACKWARD MOVEMENT
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                self.rotation = 1
            elif i.key == pygame.K_d:
                self.rotation = -1
            if i.key == pygame.K_w:
                self.motion = 1
            elif i.key == pygame.K_s:
                self.motion = -1

        # STOP MOVEMENT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_a,
                         pygame.K_d]:
                self.rotation = 0
            if i.key in [pygame.K_w,
                         pygame.K_s]:
                self.motion = 0