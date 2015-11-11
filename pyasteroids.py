''' This is the main program, it calls all the functions, when
    the game is over it returns to this function.               '''

import pygame
# Import char to pass a new char into game()
from char import char
from game import game
import os.path

# Define an ini file
def ini(width, height):
    with open('asteroids.py') as conf:
        lines = conf.readlines()
    lines[0].replace('res:')
    lines[1].replace('width=' + str(width))
    lines[2].replace('height=' + str(height))

# Define the method
def main():
    # Get ini file. This includes, primarily screen resolution:
    if os.path.isfile('asteroids.ini'):
        conf = open('asreroids.ini', 'r+w')
        switch = conf.readline()
        if switch == 'res:':
            w = conf.readline()
            w = w.split('=')
            width = w[1]
            h = conf.readline()
            h = h.split('=')
            height = h[1]
        # If the ini file isn't formatted properly, give a dialog box
        # and ask them if they'd like to create a valid ini file
        else:
            # TODO
    # If there is no ini file, create one
    else:
        ini(800,600)
        width = 800
        height = 600
    
    # Start pygame
    pygame.init()

    # Define the screen
    size = (width, height)
    screen = pygame.display.set_mode(size)
    # Window name
    pygame.display.set_caption("PyAsteroids")
    
    while 

