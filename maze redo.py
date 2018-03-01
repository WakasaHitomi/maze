# Imports
import pygame
import intersects


''' covert rects on player 1'''
# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
TITLE = "Cat Escape"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


#images
cat1 = pygame.image.load('maze cat-1.png')

# Make a player
player_rect = [10, 850, 40, 40]
vel1 = [0, 0]
player1_speed = 8
score = 0

def cat_player(player_rect):
    loc = player_rect[:2]

    screen.blit(cat1, loc)
    



player2 = [300, 150, 25, 25]
vel2 = [0, 0]
player2_speed = 8
score = 0

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 435, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [75, 495, 200, 80]

walls = [wall1, wall2, wall3, wall4]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up1 = pressed[pygame.K_UP]
    down1 = pressed[pygame.K_DOWN]
    left1 = pressed[pygame.K_LEFT]
    right1 = pressed[pygame.K_RIGHT]

    if left1:
        vel1[0] = -player1_speed
    elif right1:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up1:
        vel1[1] = -player1_speed
    elif down1:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player_rect[0] += vel1[0]
    player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player_rect, w):        
            if vel1[0] > 0:
                player_rect[0] = w[0] - player_rect[2]
            elif vel1[0] < 0:
                player_rect[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player_rect[1] += vel1[1]
    player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player_rect, w):                    
            if vel1[1] > 0:
                player_rect[1] = w[1] - player_rect[3]
            if vel1[1]< 0:
                player_rect[1] = w[1] + w[3]


    #''' here is where you should resolve player collisions with screen edges '''
    ''' get block edges (makes collision resolution easier to read) '''
    left = player_rect[0]
    right = player_rect[0] + player_rect[2]
    top = player_rect[1]
    bottom = player_rect[1] + player_rect[3]

    ''' if the block is moved completely off of the window, reposition it on the other side '''
    if left < 0:
        player_rect[0] = 0
    elif right > WIDTH:
        player_rect[0] = WIDTH - player_rect[2]

    if top < 0:
        player_rect[1] = 0
    elif bottom > HEIGHT:
        player_rect[1] = HEIGHT - player_rect[3]






    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player_rect, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, BLACK, player_rect)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    cat_player(player_rect)
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
