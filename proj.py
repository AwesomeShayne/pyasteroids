''' This is the class that handles projectiles, which is how
    we destroy asteroids                                    '''

import pygame
from game_object import game_object
from math import cos, sin, radians, hypot
from os.path import join as file

class proj(game_object):
    # Create a projectile, this is temporarily the only thing for 
    # this class to do.
    def __init__(self, angle, loc, scale):
        self.acc = 0
        ang = -radians(angle)
        i_value = cos(ang)
        j_value = sin(ang)
        i = 20 * i_value
        j = 20 * j_value
        self.vel = [i,j]
        self.loc = loc[:]
        self.angle = 0
        image = pygame.image.load(file('data','circle.png')).convert_alpha()
        if scale == [1, 1]:
            self.im = pygame.transform.smoothscale(image, [4,4])
        else:
            self.im = pygame.transform.smoothscale(image, [4*scale[0], 4*scale[1]])
        self.rect = self.im.get_rect()
        self.mask = pygame.mask.from_surface(self.im)
        self.mask.fill()
        self.max_distance = 500
        self.dist = 0

    # Override the move function so that the projectile 
    # can have limited distance.
    def move(self, screen):
        if self.dist <= self.max_distance:
            self.loc[0] += self.vel[0]
            self.loc[1] += self.vel[1]
            self.dist += hypot(self.vel[0], self.vel[1])
            self.rect.topleft = self.loc[0], self.loc[1]
            self.wrap(screen)
            return True 
        else:
            return False
