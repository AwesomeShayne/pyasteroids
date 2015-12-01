''' This class handles the asteroids, including breaking into
    smaller asteroids and later handling the dropping of powerups '''

import pygame
from random import randint
from math import sin, cos, radians, hypot, atan, pi, pow
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
            self.radius = hypot(50 * scale[0], 50 * scale[1])
            self.score = 20
            self.mass = 9
        elif size == 2:
            if scale == [1, 1]:
                self.im = image.convert_alpha()
            else:
                self.im = pygame.transform.scale(image,
                        [50 * scale[0], 50 * scale[1]]).convert_alpha()
            self.radius = hypot(25 * scale[0], 25 * scale[1])
            self.score = 50
            self.mass = 3
        elif size == 1:
            if scale == [1, 1]:
                self.im = pygame.transform.scale(image,
                        [25, 25]).convert_alpha()
            else:
                self.im = pygame.transform.scale(image,
                        [25 * scale[0], 25 * scale[1]]).convert_alpha()
            self.radius = hypot(12.5 * scale[0], 12.5 * scale[1]) 
            self.score = 100
            self.mass = 1
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
            loc[0] = loc[0] + randint(-10, 10)
            loc[1] = loc[1] + randint(-10, 10) 
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
    
    # These functions return and set information for collision
    def get_vel(self):
        return self.vel
    def get_vel_hat(self):
        vel_mag = hypot(self.vel[0], self.vel[1])
        vel_hat = [self.vel[0]/vel_mag, self.vel[1]/vel_mag]
        return vel_hat
    def get_mass(self):
        return self.mass
    def set_vel(self, vel):
        self.vel = vel
    def get_rvect(self,point):
        c = self.mask.centroid()
        angle_vector = [c[0] - point[0], c[1] - point[1]]
        return angle_vector
    def get_cent(self):
        return self.loc

    # Bouncy Asteroids!!! This function is designed to handle the elastic
    # collisions involved between two asteroids.
    def elastic_collision(self, roid, point):
        m_1 = self.get_mass()
        m_2 = roid.get_mass()
        vel_1 = self.get_vel()
        vel_2 = roid.get_vel()
        cent_1 = self.get_cent()
        cent_2 = self.get_cent()
        rad_1 = self.get_rvect(point)
        rad_2 = roid.get_rvect(point)
        
        offset = [int(roid.loc[0]) -  int(self.loc[0]),
                int(roid.loc[1]) - int(self.loc[1])]
        offdist = hypot(offset[0], offset[1])
        
        overlap = self.mask.overlap_area(roid.mask, offset)

        vel_1f[0] = vel_1[0] - ( (2 * m_2) / (m_1 + m_2) * ( (
            ( (vel_1[0] - vel_2[0]) * (cent_1[0] - cent_2[0]) ) + 
            ( (vel_1[1] - vel_2[1]) * (cent_1[1] - cent_2[1]) ) ) /
            ( (pow(cent_1[0] - cent_2[0],2) + pow(cent_1[1] - cent_2[1]) ) ) ) *
            (cent_1[0] - cent_2[0]) )
            
        vel_1f[1] = vel_1[1] - ( (2 * m_2) / (m_1 + m_2) * ( (
            ( (vel_1[0] - vel_2[0]) * (cent_1[0] - cent_2[0]) ) + 
            ( (vel_1[1] - vel_2[1]) * (cent_1[1] - cent_2[1]) ) ) /
            ( (pow(cent_1[0] - cent_2[0],2) + pow(cent_1[1] - cent_2[1]) ) ) ) *
            (cent_1[1] - cent_2[1]) )
        
        vel_2f[0] = vel_2[0] - ( (2 * m_1) / (m_2 + m_1) * ( (
            ( (vel_2[0] - vel_1[0]) * (cent_2[0] - cent_1[0]) ) + 
            ( (vel_2[1] - vel_1[1]) * (cent_2[1] - cent_1[1]) ) ) /
            ( (pow(cent_2[0] - cent_1[0],2) + pow(cent_2[1] - cent_1[1]) ) ) ) *
            (cent_2[0] - cent_1[0]) )
            
        vel_2f[1] = vel_2[1] - ( (2 * m_1) / (m_2 + m_1) * ( (
            ( (vel_2[0] - vel_1[0]) * (cent_2[0] - cent_1[0]) ) + 
            ( (vel_2[1] - vel_1[1]) * (cent_2[1] - cent_1[1]) ) ) /
            ( (pow(cent_2[0] - cent_1[0],2) + pow(cent_2[1] - cent_1[1]) ) ) ) *
            (cent_2[1] - cent_1[1]) )
        
        vmag_1f = hypot(vel_1f[0], vel_1f[1])
        vmag_2f = hypot(vel_2f[0], vel_2f[1])

        KE1 = m_1 * pow(vmag_1, 2) + m_2 * pow(vmag_2, 2)
        KE2 = m_1 * pow(vmag_1f, 2) + m_2 * pow(vmag_2, 2)
        
        print(KE1)
        print(KE2)

        roid.set_vel(vel_2f)
        self.set_vel(vel_1f)
         
        offset = [int(roid.loc[0]) -  int(self.loc[0]),
                int(roid.loc[1]) - int(self.loc[1])]
        offdist = hypot(offset[0], offset[1])
        overlap = self.mask.overlap_area(roid.mask, offset)
        if overlap > 1:
            nx = (self.mask.overlap_area(roid.mask, (offset[0] + 1, offset[1])) -
                    self.mask.overlap_area(roid.mask, (offset[0] - 1, offset[1])))
            ny = (self.mask.overlap_area(roid.mask, (offset[0], offset[1] + 1)) - 
                    self.mask.overlap_area(roid.mask, (offset[0], offset[1] - 1)))
            
            nm = hypot(nx,ny)
    
            nh = [nx/nm, ny/nm]
    
            if offdist < (self.radius + roid.radius):
                over = self.radius + roid.radius - offdist
                self.loc[0] = self.loc[0] + over * nh[0]
                self.loc[1] = self.loc[1] + over * nh[1]


