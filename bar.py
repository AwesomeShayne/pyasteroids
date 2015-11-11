''' This class exists to fill an apparent void in pygame to allow
    a bar of given dimensions and a given ratio to be displayed.
    this bar accepts several values and can be made to follow a 
    sprite by including it in the update, move, or draw methods 
    of the sprite and feeding it a relative location.           '''

import pygame

class bar():
    def __init__(self, max, size, loc, color, scale):
        self.max = max
        self.current = max
        self.size = size
        self.loc = loc
        self.color = color
        self.im = pygame.Surface((size))
        self.pts = [[0,0],[size[0],0],[size[0]-1,size[1]-1],[0,size[1-1]]]
        self.rat_rect = pygame.Rect((0,0), (size[0],size[1]))

    def change_current(self, delta):
        self.current += delta

    def set_current(self, new_current):
        self.current = new_current

    def set_max(self, new_max):
        self.max = new_max

    def get_max(self):
        return self.max

    def get_current(self):
        return self.current

    def set_color(self, color):
        self.color = color

    def update_bar(self):
        self.im.fill([0,0,0])
        ratio = self.current/self.max
        rat_fill = ratio*self.size[0]
        self.rat_rect = pygame.Rect((0,0), (rat_fill,self.size[1]))

    def draw(self, screen):
        pygame.draw.lines(self.im, self.color, True, self.pts)
        pygame.draw.rect(self.im, self.color, self.rat_rect)
        screen.blit(self.im, self.loc)
