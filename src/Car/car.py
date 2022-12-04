import pygame

import math

from settings import WIDTH, HEIGHT


class BaseCar:
    rotate_speed: int = 3
    move_speed: int = 4

    def __init__(self, sprite_path: str):
        sprite = pygame.image.load(sprite_path).convert_alpha()

        self.car = pygame.transform.smoothscale(
            sprite, (sprite.get_width() // 2, sprite.get_height() // 2)
        )

        self.car_rect = self.car.get_rect(center=(self.x, self.y))
        self.car_clean = self.car.copy()

        self.rotation = 0
        self.motion = 0

    def update_rect(self) -> None:
        self.car = pygame.transform.rotate(self.car_clean, self.degree)
        self.car_rect = self.car.get_rect(center=(self.x, self.y))

    def on_pygame_event(self, event: pygame.event) -> None:
        pass

    def update() -> None:
        raise NotImplementedError

    def process(self):
        self.process_rotation()
        self.process_motion()

        self.update_rect()

    def process_rotation(self) -> None:
        if self.rotation == 0:
            return

        self.degree += self.rotate_speed * self.rotation
        if self.degree >= 180:
            self.degree -= 180
            if self.degree == 0:
                self.degree = -180

    def process_motion(self) -> None:
        if self.motion == 0:
            return

        self.x -= math.sin(math.radians(self.degree)) * self.move_speed * self.motion
        self.y -= math.cos(math.radians(self.degree)) * self.move_speed * self.motion
