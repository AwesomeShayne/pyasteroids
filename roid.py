''' This class handles the asteroids, including breaking into
    smaller asteroids and later handling the dropping of powerups '''

import pygame
from random import randint
from math import sin, cos, radians, hypot
from game_object import game_object
from os.path import join as file

class roid(game_object):
    # Create new roids with a minimum distance from the 
    def __init__(self, size, screensize, boom, loc):
        self.size = size
        loc = loc[:]
        if boom != True:
            while 1:
                local_x = randint(0,screensize[0])
                local_y = randint(0,screensize[1])
                dist_x = local_x - loc[0]
                dist_y = local_y - loc[1]
                dist = hypot(dist_x,dist_y)
                if dist <= 300:
                    self.loc = [local_x,local_y]
                    break
        else:
            loc[0] = loc[0] + randint(-10,10)
            loc[1] = loc[1] + randint(-10,10)
            if loc[0] < 0:
                loc[0] += screensize[0]
            elif loc[0] > screensize[0]:
                loc[0] -= screensize[0]
            if loc[1] < 0:
                loc[1] += screensize[1]
            elif loc[1] > screensize[1]:
                loc[1] -= screensize[1]
            self.loc = loc

        self.angle = randint(0,360)
        vel = (4-size)
        ang = radians(self.angle)
        i_value = cos(ang)
        j_value = sin(ang)
        i = vel * i_value
        j = vel * j_value
        self.vel = [i ,j]
        image = pygame.image.load(file('data','circle.png')).convert_alpha()
        if (size == 3):
            self.im = pygame.transform.scale2x(image)
        elif size == 2:
            self.im = image
        elif size == 1:
            self.im = pygame.transform.scale(image, [32, 32])
        self.rect = self.im.get_rect()

    def explode(self, screensize):
        roids = []
        if self.size > 1:
            for x in range(0,3):
                roids.append(roid(self.size-1,screensize, True, self.loc))
        return roids




