import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1028, 724)
screen = pygame.display.set_mode(size)

# Set the Window Name
pygame.display.set_caption("PyAsteroids")

# Define Global Variables

# Initialize Character Variables

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
        if event.type == pygame.KEYUP:
    # --- Game logic should go here
 
    # --- Drawing code should go here
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
