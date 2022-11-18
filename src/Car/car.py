import pygame

import math

from settings import WIDTH, HEIGHT

speed_rotate, speed_forward = 3, 4

class Car:
    def create(self, arg):
        car = pygame.image.load(arg).convert_alpha()

        self.car = pygame.transform.smoothscale(car, 
            (car.get_width()//2, car.get_height()//2))
        
        self.car_rect = self.car.get_rect(center=(self.x, self.y))
        
        self.car_clean = self.car.copy()

        self.rotation = 0
        self.motion = 0

    def drive(self):
        # MOTION LOGIC
        if self.rotation or self.motion:
            # SOLUTION THROUGH A TRIGONOMETRIC CIRCLE
            # JUST A CAR NOW IS A SIDE OF A CORNER
            if self.rotation:
                self.degree += speed_rotate * self.rotation
                self.car = pygame.transform.rotate(self.car_clean, self.degree)
                self.car_rect = self.car.get_rect(center=(self.x, self.y))
                if self.degree >= 180:
                    self.degree -= 180
                    if self.degree == 0:
                        self.degree = -180


            if self.motion:
                self.x -= math.sin(math.radians(self.degree)) * speed_forward * self.motion
                self.y -= math.cos(math.radians(self.degree)) * speed_forward * self.motion
                self.car_rect = self.car.get_rect(center=(self.x, self.y))
