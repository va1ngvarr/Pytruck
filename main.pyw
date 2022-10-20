'''
name: Pytruck
author: Igor Vasiljev
email: va1ngvarr@outlook.com
link: https://github.com/va1ngvarr/Truck-Pygame
'''

import pygame
from pygame.locals import *

import sys

from Car import Bot, Player
from settings import WIDTH, HEIGHT, FPS

# INITIALIZATION AND PARAMETERS
pygame.init()
main_sc = pygame.display.set_mode((WIDTH, HEIGHT))
frame_limit = pygame.time.Clock().tick

amount_bot = 2

def main():
    player = Player()

    bots = [Bot() for x in range(amount_bot)]

    while True:
        frame_limit(FPS)

        # EVENT HANDLING
        for i in pygame.event.get():
            # EXIT
            if i.type == pygame.QUIT:
                sys.exit()
            player.bindings(i)

        # BACKGROUND FILL AND CAR DRAWING
        main_sc.fill((255, 255, 255))

        main_sc.blit(player.car, player.car_rect)
        
        for x in range(amount_bot):
            main_sc.blit(bots[x].car, bots[x].car_rect)
            bots[x].self_driving()
            bots[x].drive()

        player.drive()

        pygame.display.update()


if __name__ == '__main__':
    main()
