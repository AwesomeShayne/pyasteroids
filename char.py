''' This class is defined to take care of the things that have to
    be done by the character, namely fire and have handle powerups '''

import pygame
from game_object import game_object
from os.path  import join as file
from math import cos, sin, radians
from proj import proj

class char(game_object):
    # This constructor handles all character information
    def __init__(self, screensize, image, thrust, rotor):
        self.acc = 0
        self.vel = [0, 0]
        loc_x = int(screensize[0]/2)
        loc_y = int(screensize[1]/2)
        self.loc = [loc_x, loc_y]
        self.thrust = thrust
        self.angle = 0
        self.rotor = rotor
        self.rot = 0
        self.im = pygame.image.load(file('data', 'triangle.png')).convert_alpha()
        self.consumption = 0
        self.fuel = 1000
        self.rect = self.im.get_rect()
    # This handles thrust
    def thrusters(self):
        self.acc += self.thrust
        self.consumption += 1

    # This handles stopping thrust
    def thrusters_off(self):
        self.acc -= self.thrust
        self.consumption += 1
        
    # This handles acceleration, taking into account angle
    # and applying the force in the proper direction
    def accelerate(self):
        if self.acc != 0:
            ang = -radians(self.angle)
            i_value = cos(ang)
            j_value = sin(ang)
            i = self.acc * i_value
            j = self.acc * j_value
            self.vel[0] += i
            self.vel[1] += j
            self.fuel -= self.consumption

    # This function handles whether or not to rotate
    def rotate_on(self, direction):
        self.rot = direction * self.rotor

    # This function disables rotation
    def rotate_off(self):
        self.rot = 0
        
    # This function handles firing
    def fire(self):
        loc = self.loc
        pro = proj(self.angle,loc)
        return pro
