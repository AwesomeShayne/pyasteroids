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
    def move(self, screen):
        self.loc[0] += self.vel[0]
        self.loc[1] += self.vel[1]
        self.rect.center = self.loc
        self.wrap(screen)

    # This function is in charge of rotating the object
    def rotate(self):
        self.angle += self.rot

    # This function draws the object and fully handles image rotation
    # and collision-mask/image centering.
    def draw(self, screen):
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.im,
                (self.angle-90)).convert_alpha()
        self.rect = rot_image.get_rect(center=orig_rect.center)
        new_loc = [self.loc[0] - self.rect.width / 2,
                self.loc[1] - self.rect.height / 2]
        self.mask = pygame.mask.from_surface(rot_image)
        screen.blit(rot_image, new_loc)

    # Defined for screen wrapping purposes:
    def wrap(self, screen):
        if self.loc[0] < 0:
            self.loc[0] += screen[0]
        elif self.loc[0] > screen[0]:
            self.loc[0] -= screen[0]
        if self.loc[1] < 0:
            self.loc[1] += screen[1]
        elif self.loc[1] > screen[1]:
            self.loc[1] -= screen[1]
