import math #some more advanced math
import random #supppppeeerrrr important for games
import pygame #set up a display window, characters, enemies, and make them move
from pygame import mixer



#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,500))

#create background
background = pygame.image.load('5808D365-5D16-4CEA-A742-8B282A3F76E9.jpg')
background = pygame.transform.scale(background, (800, 500)) 

#import music
#mixer.music.load('background.mp3')
#mixer.music.play(-1)

  
#initialize player character
playerImg = pygame.image.load('player.png').convert_alpha()
playerImg.set_colorkey((255,255,255))
playerImg = pygame.transform.scale(playerImg, (50, 50)) 
playerX = 370
playerY = 380
playerX_change = 0

#obstacles
enemyImg = []
enemyX = [] 
enemyY = []
enemyX_change = [] 
enemyY_change = [] 
num_enemies = 10


for i in range(num_enemies):
    enemyImg.append(pygame.image.load('evilblob.png').convert())
    enemyImg[i].set_colorkey((255,255,255))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (38, 38)) 
    enemyX.append(random.randint(100, 662))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0)
    enemyY_change.append(5)

#power ups
powerImg = []
powerX = [] 
powerY = []
powerX_change = [] 
powerY_change = [] 

powerImg.append(pygame.image.load('power1.jpg').convert())
powerImg[0].set_colorkey((255,255,255))
powerImg[0] = pygame.transform.scale(powerImg[0], (38, 38))
powerX.append(random.randint(100, 662))
powerY.append(random.randint(50,150))
powerX_change.append(0)
powerY_change.append(2)

    
#scoring
score = 0
font = pygame.font.Font('FreeSansBold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('FreeSansBold.ttf', 64)

# show score
def show_score(x,y):
    score_disp = font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score_disp, (x,y))

# show game over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (200,250))

# display player
def player(x,y):
    screen.blit(playerImg, (x,y))

# display enemies
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

#dispaly power up
def power(x,y,i):
    screen.blit(powerImg[i], (x,y))

# define collision
def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX-playerX,2) + (math.pow(enemyY-playerY,2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
hearts = 3
clock = pygame.time.Clock()
pause = 1
score_passed = 0
power_up = 0
powered_up = 0
movement = 7
while running:
    
    if(hearts <= 0):
        # game over loop 
        while True:
            screen.fill((0,0,0))

            # background image
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            game_over_text()
            pygame.display.update()
            clock.tick(60)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    hearts = 5
                    score = 0
                    break
        
    screen.fill((0,0,0))
    
    # background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(score % 500 == 0 and score != 0 and score != score_passed):
        for i in range(num_enemies):
            enemyY_change[i] = enemyY_change[i] + 1
            score_passed = score
    
    if (pause == 1):
        while(True):
            if event.type == pygame.KEYDOWN:
                pause = 0
                break
            screen.fill((0,0,0))

            screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            player(playerX, playerY)
            show_score(textX, textY)
            pygame.display.update()
            clock.tick(60)

    # checking keystrokes
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -1 * movement
        if event.key == pygame.K_RIGHT:
            playerX_change = movement

    # setting player boundaries 
    playerX += playerX_change
    if playerX <= 100:
        playerX = 100
    elif playerX >= 650:
        playerX = 650
    playerX_change = 0

    # managing enemy movement
    for i in range(num_enemies):
        enemy(enemyX[i],enemyY[i],i)
        if enemyY[i] > 450:
            score += 1
            enemyY[i] = 0
            enemyX[i] = random.randint(100,662)
            break
        enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision:
            hearts -= 1
            score -= 50
            enemyX[i] = random.randint(100,662)
            enemyY[i] = 0

    if(power_up == 0):
        chance = random.randint(1,600)
    if (chance == 326):
        power_up = 1
        power(powerX[0], powerY[0], 0)
        if powerY[0] > 450:
            powerY[0] = 0
            powerX[0] = random.randint(100,662)
            power_up = 0
        powerY[0] += powerY_change[0]

        collision = isCollision(powerX[0], powerY[0], playerX, playerY)
        if collision:
            power_up = 0
            powerX[0] = random.randint(100,662)
            powerY[0] = 0
            powered_up = 1
            counter = 0

        if(powered_up):
            movement = 14
            counter += 1
            if(counter >= 240):
                powered_up = 0
                movement = 7
            
            

        
    player(playerX, playerY)
    
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)



 #SHOW THE HEARTS IN  GAME!!!!!!!!
 #DO FINAL TWEAKS
 # PUT IT ONLINE
 




    
    








    
