import pygame
from char import char
from proj import proj
from roid import roid as new_roid


# Define Global Variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

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
scale = [1, 1]

char = char(size, 'triangle.png', .05, 2, scale)
    

# Define define game loop function:
def game(screen, char, level):
    char = char 
    roids = []
    sc_x = screen.get_width()
    sc_y = screen.get_height()
    scale = []
    scale.append(sc_x/1024)
    scale.append(sc_y/768)
    for x in range(0,4):
        ro = new_roid(3, size, False, char.rect.center, scale)
        roids.append(ro)
    
    projs = []


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
                if event.key == pygame.K_RIGHT:
                    char.rotate_off(-1)
                if event.key == pygame.K_LEFT:
                    char.rotate_off(1)
        # --- Game logic should go here
        char.accelerate()
        char.rotate()
        char.move(size)
        for roid in roids:
            roid.move(size)
            for r in roids:
                if r != roid:
                    if pygame.sprite.collide_mask(roid, r) != None:
                        print(str(pygame.sprite.collide_mask(roid, r)))
                        p = pygame.sprite.collide_mask(roid, r)
                        roid.elastic_collision(r,p)
            if pygame.sprite.collide_mask(roid, char) != None:
                if char.hit():
                    if char.lives_left():
                        char.respawn(size)
                    else:
                        done = True
        for proj in projs[:]:
            live = proj.move(size)
            if live:
                for roid in roids[:]:
                    if (pygame.sprite.collide_mask(proj, roid) != None) or (pygame.sprite.collide_mask(roid, proj) != None):
                        projs.remove(proj)
                        roids.remove(roid)
                        char.scoreup(roid.score)
                        if char.get_life_score():
                            char.add_life()
                        n = roid.explode([SCREEN_WIDTH, SCREEN_HEIGHT])
                        for r in n:
                            roids.append(r)
                        break       
            else:
                projs.remove(proj)
        if not roids:
            done = True
            game(screen, char, level+1)
        score = char.get_score()
        fuel = char.get_fuel()
        font = pygame.font.Font(None, 36)        
        score = char.get_score()
        score_text = font.render(str(score), 1, (255, 255, 255))
        score_pos = score_text.get_rect()
        score_pos.centerx = screen.get_rect().centerx
        # --- Drawing code should go here
        screen.fill(BLACK)
        for roid in roids:
            roid.draw(screen)
        for proj in projs:
            proj.draw(screen)
        char.draw(screen)
        screen.blit(score_text, score_pos)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    pygame.quit()
game(screen, char, 1)
