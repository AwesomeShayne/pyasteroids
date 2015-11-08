''' This is the class that handles projectiles, which is how
    we destroy asteroids                                    '''

import pygame
from game_object import game_object
from math import cos, sin, radians

class proj(game_object):
    # Create a projectile, this is temporarily the only thing for 
    # this class to do.
    def __init__(self, angle, loc):
        self.acc = 0
        ang = -radians(angle)
        i_value = cos(ang)
        j_value = sin(ang)
        i = 20 * i_value
        j = 20 * j_value
        self.vel = [i,j]
        self.loc = loc[:]
        self.angle = 0
        self.im = pygame.Surface([4,4])
        self.im.fill([255,255,255])
        self.rect = self.im.get_rect()
        self.mask = pygame.mask.from_surface(self.im)
