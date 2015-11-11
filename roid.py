''' This class handles the asteroids, including breaking into
    smaller asteroids and later handling the dropping of powerups '''

import pygame
from random import randint
from math import sin, cos, radians, hypot
from game_object import game_object
from os.path import join as file

class roid(game_object):
    # Create new roids with a minimum distance from the 
    def __init__(self, size, screensize, boom, loc, scale):
        self.size = size
        self.angle = randint(0,360)
        self.scale = scale
        vel = (4-size)
        ang = radians(self.angle)
        i_value = cos(ang)
        j_value = sin(ang)
        i = vel * i_value
        j = vel * j_value
        self.vel = [i ,j]
        image = pygame.image.load(file('data','circle.png')).convert_alpha()
        if (size == 3):
            if scale == [1, 1]:
                self.im = pygame.transform.scale2x(image).convert_alpha()
            else:
                self.im = pygame.transform.scale(image,
                        [100 * scale[0], 100 * scale[1]]).convert_alpha()
            self.score = 20
        elif size == 2:
            if scale == [1, 1]:
                self.im = image.convert_alpha()
            else:
                self.im = pygame.transform.scale(image,
                        [50 * scale[0], 50 * scale[1]]).convert_alpha()
            self.score = 50
        elif size == 1:
            if scale == [1, 1]:
                self.im = pygame.transform.scale(image,
                        [25, 25]).convert_alpha()
            else:
                self.im = pygame.transform.scale(image,
                        [25 * scale[0], 25 * scale[1]]).convert_alpha()
            self.score = 100
        self.rect = self.im.get_rect()
        self.mask = pygame.mask.from_surface(self.im)
        self.mask.fill()
        loc = loc[:]
        if boom != True:
            while 1:
                local_x = randint(0,screensize[0])
                local_x += self.rect.width/2
                local_y = randint(0,screensize[1])
                local_y += self.rect.height/2
                dist_x = local_x - loc[0]
                dist_y = local_y - loc[1]
                dist = hypot(dist_x,dist_y)
                if dist >= 300:
                    self.loc = [local_x,local_y]
                    break
        else:
            loc[0] = loc[0] + randint(-10,10)
            loc[1] = loc[1] + randint(-10,10)
            self.loc = loc
            self.wrap(screensize)
    
    # When the asteroid is killed and is not the smallest size, create more
    # asteroids
    def explode(self, screensize):
        roids = []
        if self.size > 1:
            for x in range(0,3):
                roids.append(roid(self.size-1,screensize, True, self.loc, self.scale))
        return roids
    # Return the score of the asteroid
    def score(self):
        return self.score




