''' This class is defined to take care of the things that have to
    be done by the character, namely fire and have handle powerups '''

import pygame
from game_object import game_object
from os.path  import join as file
from math import cos, sin, radians, fabs
from proj import proj
from bar import bar

class char(game_object):
    # This constructor handles all character information
    def __init__(self, screensize, image, thrust, rotor, scale):
        self.acc = 0
        self.vel = [0, 0]
        loc_x = int(screensize[0]/2)
        loc_y = int(screensize[1]/2)
        self.loc = [loc_x, loc_y]
        self.thrust = thrust
        self.angle = 0
        self.rotor = rotor
        self.rot = 0
        self.scale = scale
        im = pygame.image.load(file('data', 'triangle.png')).convert_alpha()
        if scale == [1, 1]:
            self.im = im
        else:
            self.im = pygame.transform.scale(im, [50*scale[0], 50*scale[1]])
        self.consumption = 0
        self.fuel = 1000
        self.rect = self.im.get_rect()
        self.mask = pygame.mask.from_surface(self.im)
        self.rect.topleft = self.loc[0], self.loc[1]
        self.score = 0
        self.color = [255, 255, 255]
        barsize = [scale[0] * 200, scale[1] * 20]
        bar_loc = [screensize[0]-barsize[0]-30*scale[0], 10*scale[1]]
        self.fuelbar = bar(1000, barsize, bar_loc, self.color, scale)
        self.lives = 3
        self.invuln = True
        self.invuln_timer = 180
        self.extra_count = 0

    # This handles thrust
    def thrusters(self):
        if self.fuel > 0:
            self.acc += self.thrust
            self.consumption -= 1

    # This handles stopping thrust
    def thrusters_off(self):
        self.acc -= self.thrust
        self.consumption += 1
        
    # This handles acceleration, taking into account angle
    # and applying the force in the proper direction
    def accelerate(self):
        if self.invuln:
            self.invuln_timer -= 1
            if self.invuln_timer  <= 0:
                self.invuln = False
 
        if self.acc != 0:
            ang = -radians(self.angle)
            i_value = cos(ang)
            j_value = sin(ang)
            i = self.acc * i_value
            j = self.acc * j_value
            self.vel[0] += i
            self.vel[1] += j
            self.fuel += self.consumption
            self.fuelbar.change_current(self.consumption)
            self.fuelbar.update_bar()
                    

    # This function handles whether or not to rotate
    def rotate_on(self, direction):
        self.rot = direction * self.rotor

    # This function disables rotation
    def rotate_off(self, direction):
        if (self.rot == direction * self.rotor):
            self.rot -= (direction * self.rotor)
        
    # This function handles firing
    def fire(self):
        loc = self.loc
        pro = proj(self.angle,loc, self.scale)
        return pro

    # Scoring
    def scoreup(self, score):
        self.score += score

    # Return Score
    def get_score(self):
        return self.score

    # Return Fuel
    def get_fuel(self):
        return self.fuel

    # Override Draw to draw bar
    def draw(self, screen):
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.im, (self.angle-90))
        self.rect = rot_image.get_rect(center=orig_rect.center)
        new_loc = [self.loc[0] - self.rect.width / 2,
                self.loc[1] - self.rect.height / 2]
        self.mask = pygame.mask.from_surface(rot_image)
        pts = self.mask.outline()
        masksurf = pygame.Surface((50*self.scale[0],50*self.scale[1]))
        screen.blit(rot_image, new_loc)
        self.fuelbar.draw(screen)

    # If collided, calls this
    def hit(self):

        if self.invuln == False:
            self.lives -= 1
            return True
        else:
            return False

    # Get lives
    def lives_left(self):
        if self.lives > 0:
            return True
        else:
            return False

    # Respawn if lives are left:
    def respawn(self, size):
        self.invuln = True
        self.invuln_timer = 180
        self.acc = 0
        self.vel = [0, 0]
        self.loc[0] = size[0]/2
        self.loc[1] = size[1]/2
        self.angle = 0
        self.fuel = 1000
        self.fuelbar.set_current(1000)

    # This keeps track of the score requirements for more lives
    def get_life_score(self):
        life_score = self.score/10000
        if life_score > extra_count:
            return True
        else:
            return False

    # Get life, this is for if score is high enough, and if a pickup
    # grants a life.
    def add_life(self):
        self.lives += 1

