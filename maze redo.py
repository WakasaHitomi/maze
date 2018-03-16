
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
BGGREEN = (1, 114, 6)





#images
cat1 = pygame.image.load('maze cat-1.png')

cat2 = pygame.image.load('maze cat-1.png')

cat3 = pygame.image.load('maze cat-1.png')



fishy1 = pygame.image.load('fish-1.png')
fishy2= pygame.image.load('fish-2.png')
fishy3 = pygame.image.load('fish-3.png')
fishy4 = pygame.image.load('fish-4.png')
fishy5= pygame.image.load('fish-2.png')
fishy6 = pygame.image.load('fish-3.png')
fishy7 = pygame.image.load('fish-4.png')
fishy8 = pygame.image.load('fish-2.png')

fishy_treat = [fishy1, fishy2, fishy3, fishy4, fishy5, fishy6, fishy7, fishy8]

# Make a player
player_rect = [10, 150, 40, 40]
vel1 = [0, 0]
player1_speed = 8
score = 0

def cat_player1(player_rect):
    loc = player_rect[:2]

    screen.blit(cat1, loc)

    


player2_rect = [300, 150, 40, 40]
vel2 = [0, 0]
player2_speed = 8
score = 0


def cat_player2(player2_rect):
    loc2 = player2_rect[:2]

    screen.blit(cat2, loc2)



player3_rect = [300, 150, 40, 40]
vel3 = [0, 0]
player3_speed = 8
score = 0


def cat_player3(player3_rect):
    loc3 = player3_rect[:2]

    screen.blit(cat3, loc3)

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 435, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [75, 495, 200, 80]
wall5 = [0, 580, 200, 20] 

walls = [wall1, wall2, wall3, wall4, wall5]

# Make coins






'''fixing coin fish treat shift....... try doing it backwards, like making the picture into a coin...? like the imge asa function and the coin being called only for location,but sameprocessing of a coin'''
#picture into a coin



#New test code for coins

fish_rect1 = [300, 300, 25, 25]
fish_rect2 = [300, 350, 25, 25]
fish_rect3 = [375, 350, 25, 25]
fish_rect4 = [375, 300, 25, 25]

coins = [fish_rect1, fish_rect2, fish_rect3, fish_rect4]

def Jeremy(frame):
    loc = fish_rect1

    screen.blit(fishy_treat[frame], loc)

def Jeremy1(frame):
    loc = fish_rect2

    screen.blit(fishy_treat[frame], loc)

def Jeremy2(frame):
    loc = fish_rect3

    screen.blit(fishy_treat[frame], loc)


def Jeremy3(frame):
    loc = fish_rect4

    screen.blit(fishy_treat[frame], loc)
    
    

blacked = [Jeremy, Jeremy1, Jeremy2, Jeremy3]


# Fonts
MY_FONT = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global block_pos, block_vel, size, stage, time_remaining, ticks
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START
    time_remaining = 90
    ticks = 0

# Game loop# Fonts
MY_FONT = pygame.font.Font(None, 90)

MY_FONT2 = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2

setup()
done = False

    
# Game loop
win = False
done = False

tick = 0
frame = 0

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                
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






                up2 = pressed[pygame.K_w]
                down2 = pressed[pygame.K_s]
                left2 = pressed[pygame.K_a]
                right2 = pressed[pygame.K_d]

                if left2:
                    vel2[0] = -player2_speed
                elif right2:
                    vel2[0] = player2_speed
                else:
                    vel2[0] = 0

                if up2:
                    vel2[1] = -player2_speed
                elif down2:
                    vel2[1] = player2_speed
                else:
                    vel2[1] = 0



                up3 = pressed[pygame.K_u]
                down3 = pressed[pygame.K_j]
                left3 = pressed[pygame.K_h]
                right3 = pressed[pygame.K_k]

                if left3:
                    vel3[0] = -player3_speed
                elif right3:
                    vel3[0] = player3_speed
                else:
                    vel3[0] = 0

                if up3:
                    vel3[1] = -player3_speed
                elif down3:
                    vel3[1] = player3_speed
                else:
                    vel3[1] = 0


            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
        
        
    # Game logic (Check for collisions, update points, etc.)
    '''timer'''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
    ''' move the player in horizontal direction '''
    player_rect[0] += vel1[0]
    player2_rect[0] += vel2[0]
    player3_rect[0] += vel3[0]

    tick += 1
    if tick%20 == 0:
        frame += 1
        if frame > 7:
            frame = 0
            
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player_rect, w):        
            if vel1[0] > 0:
                player_rect[0] = w[0] - player_rect[2]
            elif vel1[0] < 0:
                player_rect[0] = w[0] + w[2]



        if intersects.rect_rect(player2_rect, w):        
            if vel2[0] > 0:
                player2_rect[0] = w[0] - player2_rect[2]
            elif vel2[0] < 0:
                player2_rect[0] = w[0] + w[2]




        if intersects.rect_rect(player3_rect, w):        
            if vel3[0] > 0:
                player3_rect[0] = w[0] - player3_rect[2]
            elif vel3[0] < 0:
                player3_rect[0] = w[0] + w[2]



    ''' move the player in vertical direction '''
    player_rect[1] += vel1[1]
    player2_rect[1] += vel2[1]
    player3_rect[1] += vel3[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player_rect, w):                    
            if vel1[1] > 0:
                player_rect[1] = w[1] - player_rect[3]
            elif vel1[1]< 0:
                player_rect[1] = w[1] + w[3]


                
        if intersects.rect_rect(player2_rect, w):
            if vel2[1] > 0:
                player2_rect[1] = w[1] - player2_rect[3]
            elif vel2[1]< 0:
                player2_rect[1] = w[1] + w[3]



        if intersects.rect_rect(player3_rect, w):
            if vel3[1] > 0:
                player3_rect[1] = w[1] - player3_rect[3]
            elif vel3[1]< 0:
                player3_rect[1] = w[1] + w[3]


    #''' here is where you should resolve player collisions with screen edges '''
    ''' get block edges (makes collision resolution easier to read) '''
    left = player_rect[0]
    right = player_rect[0] + player_rect[2]
    top = player_rect[1]
    bottom = player_rect[1] + player_rect[3]
    
    left2 = player2_rect[0]
    right2 = player2_rect[0] + player2_rect[2]
    top2 = player2_rect[1]
    bottom2 = player2_rect[1] + player2_rect[3]

    left3 = player3_rect[0]
    right3 = player3_rect[0] + player3_rect[2]
    top3 = player3_rect[1]
    bottom3 = player3_rect[1] + player3_rect[3]
    ''' if the block is moved completely off of the window, reposition it on the other side '''
    if left < 0:
        player_rect[0] = 0
    elif right > WIDTH:
        player_rect[0] = WIDTH - player_rect[2]

    if top < 0:
        player_rect[1] = 0
    elif bottom > HEIGHT:
        player_rect[1] = HEIGHT - player_rect[3]




    if left2 < 0:
        player2_rect[0] = 0
    elif right2 > WIDTH:
        player2_rect[0] = WIDTH - player2_rect[2]

    if top2 < 0:
        player2_rect[1] = 0
    elif bottom2 > HEIGHT:
        player2_rect[1] = HEIGHT - player2_rect[3]




    if left3 < 0:
        player3_rect[0] = 0
    elif right3 > WIDTH:
        player3_rect[0] = WIDTH - player3_rect[2]

    if top3 < 0:
        player3_rect[1] = 0
    elif bottom3 > HEIGHT:
        player3_rect[1] = HEIGHT - player3_rect[3]






    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player_rect, c)]

    coins = [c for c in coins if not intersects.rect_rect(player2_rect, c)]

    coins = [c for c in coins if not intersects.rect_rect(player3_rect, c)]

    if len(coins) == 0:
        win = True

        

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BGGREEN)

    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])


    pygame.draw.rect(screen, BLACK, player_rect)
    pygame.draw.rect(screen, BLACK, player2_rect)
    pygame.draw.rect(screen, BLACK, player3_rect)


    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Catastrophe", True, WHITE)
        text2 = MY_FONT2.render("(Press SPACE to play.)", True, BLACK)
        screen.blit(text1, [420, 150])
        screen.blit(text2, [420, 350])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT2.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])



        
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
       pygame.draw.rect(screen, WHITE, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Won!", 1, GREEN)
        screen.blit(text, [400, 200])

    cat_player1(player_rect)
    cat_player2(player2_rect)
    cat_player3(player3_rect)
    Jeremy(frame)
    Jeremy1(frame)
    Jeremy2(frame)
    Jeremy3(frame)
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
