import pygame
from char import char
from proj import proj
from roid import roid


# Define Global Variables
SCREEN_WIDTH = 1028
SCREEN_HEIGHT = 724

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# Set the Window Name
pygame.display.set_caption("PyAsteroids")

# Initialize Character Variables

char = char(size, 'triangle.png', .05, 2)
roids = []
for x in range(0,4):
    ro = roid(3, size, False, char.loc)
    roids.append(ro)
    
projs = []

# Define Functions

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # --- Handle Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_UP:
                char.thrusters()
            if event.key == pygame.K_LEFT:
                char.rotate_on(1)
            if event.key == pygame.K_RIGHT:
                char.rotate_on(-1)
            if event.key == pygame.K_SPACE:
                projs.append(char.fire())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                char.thrusters_off()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                char.rotate_off()
    # --- Game logic should go here
    char.accelerate()
    char.rotate()
    char.move()
    if char.loc[0] < 0:
        char.loc[0] += SCREEN_WIDTH
    elif char.loc[0] > SCREEN_WIDTH:
        char.loc[0] -= SCREEN_WIDTH
    if char.loc[1] < 0:
        char.loc[1] += SCREEN_HEIGHT
    elif char.loc[1] > SCREEN_HEIGHT:
        char.loc[1] -= SCREEN_HEIGHT
    
    for roid in roids:
        roid.move()
        if roid.loc[0] < 0:
            roid.loc[0] += SCREEN_WIDTH
        elif roid.loc[0] > SCREEN_WIDTH:
            roid.loc[0] -= SCREEN_WIDTH
        if roid.loc[1] < 0:
            roid.loc[1] += SCREEN_HEIGHT
        elif roid.loc[1] > SCREEN_HEIGHT:
            roid.loc[1] -= SCREEN_HEIGHT
    for proj in projs[:]:
        proj.move()
        if proj.loc[0] < 0:
            proj.loc[0] += SCREEN_WIDTH
        elif proj.loc[0] > SCREEN_WIDTH:
            proj.loc[0] -= SCREEN_WIDTH
        if proj.loc[1] < 0:
            proj.loc[1] += SCREEN_HEIGHT
        elif proj.loc[1] > SCREEN_HEIGHT:
            proj.loc[1] -= SCREEN_HEIGHT
        for roid in roids[:]:
            if proj.rect.colliderect(roid.rect):
                projs.remove(proj)
                roids.remove(roid)
                n = roid.explode([SCREEN_WIDTH, SCREEN_HEIGHT])
                for r in n:
                    roids.append(r)
                break        
    # --- Drawing code should go here
    screen.fill(BLACK)
    for roid in roids:
        roid.draw(screen)
    for proj in projs:
        proj.draw(screen)
    char.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
