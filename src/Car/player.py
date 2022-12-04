import pygame

from . import BaseCar
from settings import WIDTH, HEIGHT


class PlayerCar(BaseCar):
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.degree = 0

        super().__init__("../resources/Sprites/car_player.png")

        self.car_rect = self.car.get_rect(center=(self.x, self.y))
        self.car_clean = self.car.copy()

    def bindings(self, event: pygame.event) -> None:
        # ROTATION RIGHT AND LEFT / FORWARD AND BACKWARD MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.rotation = 1
            elif event.key == pygame.K_d:
                self.rotation = -1
            if event.key == pygame.K_w:
                self.motion = 1
            elif event.key == pygame.K_s:
                self.motion = -1

        # STOP MOVEMENT
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                self.rotation = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                self.motion = 0

    def on_pygame_event(self, event: pygame.event) -> None:
        self.bindings(event)

    def update(self) -> None:
        self.process()
