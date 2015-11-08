''' This is the parent class of every object in pyasteroids.
    it contains the basic functions and parameters that all
    of these objects will need. This includes location, 
    velocity, acceleration, angle, rotation(speed), and draw. '''

import pygame

class game_object(pygame.sprite.Sprite):
    # This class needs no true constructor, it exists to make
    # its children classes more concise.
    def __init__(self):
        self.acc = 0
        self.vel = [0, 0]
        self.loc = [0, 0]
        self.angle = 0
        self.rot = 0
        self.image = pygame.Surface([16,16])
        self.im = self.image
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()

    # This function moves the object base on its velocity.
    def move(self):
        self.loc[0] += self.vel[0]
        self.loc[1] += self.vel[1]
    
    # This function is in charge of rotating the object
    def rotate(self):
        self.angle += self.rot

    # This function draws the object
    def draw(self, screen):
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.im, (self.angle-90))
        self.rect = rot_image.get_rect(center=orig_rect.center)
        new_loc = [self.loc[0] - self.rect.width / 2,
                self.loc[1] - self.rect.height / 2]
        screen.blit(rot_image, new_loc)
        self.rect = rot_image.get_rect()
        self.mask = pygame.mask.from_surface(rot_image)
        self.rect.topleft = self.loc[0], self.loc[1]
