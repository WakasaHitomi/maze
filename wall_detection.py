# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Wall Detection"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Make a block
block =  [200, 150, 50, 50]
vel = [0, 0]
speed = 5

# make a wall
wall =  [300, 275, 200, 50]


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if left:
        vel[0] = -speed
    elif right:
        vel[0] = speed
    else:
        vel[0] = 0

    if up:
        vel[1] = -speed
    elif down:
        vel[1] = speed
    else:
        vel[1] = 0
        

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block in horizontal direction '''
    block[0] += vel[0]

    ''' resolve collision '''
    if intersects.rect_rect(block, wall):
        if vel[0] > 0:
            block[0] = wall[0] - block[2]
        elif vel[0] < 0:
            block[0] = wall[0] + wall[2]

    ''' move the block in vertical direction '''
    block[1] += vel[1]
    
    ''' resolve collision '''
    if intersects.rect_rect(block, wall):
        if vel[1] > 0:
            block[1] = wall[1] - block[3]
        elif vel[1] < 0:
            block[1] = wall[1] + wall[3]


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)
    pygame.draw.rect(screen, RED, wall)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
