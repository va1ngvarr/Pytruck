from . import BaseCar
from settings import WIDTH, HEIGHT

import random


class BotCar(BaseCar):
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)

        self.degree = random.randint(-180, 180)
        super().__init__("../resources/Sprites/car_bot.png")

    # OF COURSE, I COULD TIE A NEURAL NETWORK HERE, BUT PERHAPS NOT
    # MAYBE ONCE

    def self_driving(self):
        if self.x <= 20 or self.x >= WIDTH - 20:
            self.motion = -self.motion
        elif self.y <= 20 or self.y >= HEIGHT - 20:
            self.motion = -self.motion
        else:
            if random.randint(0, 1):
                self.motion = 1
            if random.randint(0, 1):
                if random.randint(0, 1):
                    self.rotation = 1
                else:
                    self.rotation = -1

    def update(self) -> None:
        self.self_driving()
        self.process()
