import pygame
import numpy as np
pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

#loading resources

#------end lol
ballSpeedX = 5
ballSpeedY = 5
ballPos = [400,300]
ballNextPos = [0,0]
player2HitBox = []
playerHitBox = []
playerScore = 0
player2Score = 0

playerx = 20
playery = 0
player2x = 800-40
player2y = 600-100
player = pygame.Rect(playerx, playery,20,80)
player2 = pygame.Rect(player2x, player2y,20,80)
goingdown = False
goingup = False
goingdown2 = False
goingup2 = False

#273 is up 274 is down

gameDisplay = pygame.display.set_mode((800,600))
title = 'i like pennies'
pygame.display.set_caption(title)

clock = pygame.time.Clock()

crashed = False
victory = False
x,y = [0,0]

while not crashed:
    if(ballSpeedY ==0):
        ballSpeedY = -2
# --- game running ---
    # --- AI ---
    # PLAYER 2
    '''
    if(ballPos[0]>400 and ballPos[0]<410):
        ballNextPos[1] = ballPos[1]+ballSpeedY*85
        print(f'First: {ballNextPos[1]}')
        if(ballNextPos[1]<0):
            ballNextPos[1] *= -1
            print(f'Second: {ballNextPos[1]}')
        elif(ballNextPos[1]>600):
            ballNextPos[1] -= 600
            ballNextPos[1] = 600 - ballNextPos[1]
            print(f'Second: {ballNextPos[1]}')
    if(ballPos[0]>500):
        if (ballNextPos[1]>=player2y+30 and ballNextPos[1]<player2y+40):
            goingdown2 = False
            goingup2 = False
        elif(ballNextPos[1]< player2y+40):
            goingdown2 = False
            goingup2 = True
            #print(f'predicted ball position: {ballNextPos[1]}, My position:{player2y}')
        elif(ballNextPos[1]> player2y+40):
            goingdown2 = True
            goingup2 = False
            #print(f'predicted ball position: {ballNextPos[1]}, My position:{player2y}')
        
    else:
        if(player2y < 220 ):
            goingup2 = False
            goingdown2 = True
        elif(player2y+80 > 380):
            goingup2 = True
            goingdown2 = False
            
    '''
    # PLAYER 1 
    if(ballPos[0]<400 and ballPos[0]>(400+(ballSpeedX*3))):
        ishframes = 355/ballSpeedX
        ishframes = ishframes * -1
        ballNextPos[1] = ballPos[1]+ballSpeedY*int(ishframes)
        ballNextPos[0] = ballPos[0]+ballSpeedX*int(ishframes)
        print(f'First: {ballNextPos[0]};{ballNextPos[1]}, {ishframes}')
        if(ballNextPos[1]<0):
            ballNextPos[1] *= -1
            print(f'Second: {ballNextPos[1]}')
        elif(ballNextPos[1]>600):
            ballNextPos[1] -= 600
            ballNextPos[1] = 600 - ballNextPos[1]
            print(f'Second: {ballNextPos[1]}')
    if(ballPos[0]<400):
        if (ballNextPos[1]>=playery+30 and ballNextPos[1]<playery+40):
            goingdown = False
            goingup = False
        elif(ballNextPos[1]< playery+40):
            goingdown = False
            goingup = True
            #print(f'predicted ball position: {ballNextPos[1]}, My position:{player2y}')
        elif(ballNextPos[1]> playery+40):
            goingdown = True
            goingup = False
            #print(f'predicted ball position: {ballNextPos[1]}, My position:{player2y}')
        
    else:
        if(playery < 220 ):
            goingup = False
            goingdown = True
        elif(playery+80 > 380):
            goingup = True
            goingdown = False
    # --- AI END ---
    for event in pygame.event.get():
        textsurface = myfont.render(f'{playerScore} - {player2Score}', False, (255,255,255))
        gameDisplay.fill((0,0,0))

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.dict['unicode'] == 's':
                goingdown = True
                goingup = False
            elif event.dict['unicode'] == 'w':
                goingup = True
                goingdown = False
            if event.dict['key'] == 274:
                goingdown2 = True
                goingup2 = False
            elif event.dict['key'] == 273:
                goingup2 = True
                goingdown2 = False
            elif event.dict['unicode'] == 'f':
                ballSpeedX += 1

        elif event.type == pygame.KEYUP:
            if event.dict['key'] == 115:
                goingdown = False
            elif event.dict['key'] == 119:
                goingup = False
            if event.dict['key'] == 274:
                goingdown2 = False
            elif event.dict['key'] == 273:
                goingup2 = False
            if event.dict['key'] == 102:
                print(f'{playerHitBox}')
            if event.dict['key'] == 103:
                print(f'{player2HitBox}')
            
# --- change title ---
        elif event.type == pygame.MOUSEMOTION:

            x,y = event.dict['pos']
            title = f'X={x}, Y={y}'
            pygame.display.set_caption(title)
         # --- draw image ---
    if goingdown:
        if playery <= 600-80:
            playery += 5
    elif goingup:
        if playery >= 0:
            playery -= 5
    if goingdown2:
        if player2y <= 600-80:
            player2y += 5
    elif goingup2:
        if player2y >=0:
            player2y -= 5
    if ballPos[1] >= 600-7 or ballPos[1] <=0:
        ballSpeedY *= -1
    if ballPos[0]+7 >=player2x and ballSpeedX>0:
        for idx, bploop in enumerate(player2HitBox):
            if ballPos[1] == bploop:
                ballSpeedX *= -1
                if idx <=5:
                    ballSpeedY = -8
                elif idx >5 and idx <10:
                    ballSpeedY = -7
                elif idx <=10 and idx <15:
                    ballSpeedY = -6
                elif idx <=15 and idx <20:
                    ballSpeedY = -5
                elif idx <=20 and idx <25:
                    ballSpeedY = -4
                elif idx <=25 and idx <30:
                    ballSpeedY = -3
                elif idx <=30 and idx <35:
                    ballSpeedY = -2
                elif idx <=35 and idx <40:
                    ballSpeedY = -1
                elif idx <=40 and idx <45:
                    ballSpeedY = 0
                elif idx >45 and idx <50:
                    ballSpeedY = 1
                elif idx <=50 and idx <55:
                    ballSpeedY = 2
                elif idx <=55 and idx <60:
                    ballSpeedY = 3
                elif idx <=60 and idx <65:
                    ballSpeedY = 4
                elif idx <=65 and idx <70:
                    ballSpeedY = 5
                elif idx <=70 and idx <75:
                    ballSpeedY = 6
                elif idx <=75 and idx <80:
                    ballSpeedY = 7
                elif idx <=80:
                    ballSpeedY = 8
                #print(f'{bploop},{ballPos[1]}')
                break
    elif ballPos[0]-20 <= playerx and ballSpeedX<0:
        for idx,bploop in enumerate(playerHitBox):
            if ballPos[1] == bploop:
                ballSpeedX *= -1
                if idx <=5:
                    ballSpeedY = -8
                elif idx >5 and idx <10:
                    ballSpeedY = -7
                elif idx <=10 and idx <15:
                    ballSpeedY = -6
                elif idx <=15 and idx <20:
                    ballSpeedY = -5
                elif idx <=20 and idx <25:
                    ballSpeedY = -4
                elif idx <=25 and idx <30:
                    ballSpeedY = -3
                elif idx <=30 and idx <35:
                    ballSpeedY = -2
                elif idx <=35 and idx <40:
                    ballSpeedY = -1
                elif idx <=40 and idx <45:
                    ballSpeedY = 0
                elif idx >45 and idx <50:
                    ballSpeedY = 1
                elif idx <=50 and idx <55:
                    ballSpeedY = 2
                elif idx <=55 and idx <60:
                    ballSpeedY = 3
                elif idx <=60 and idx <65:
                    ballSpeedY = 4
                elif idx <=65 and idx <70:
                    ballSpeedY = 5
                elif idx <=70 and idx <75:
                    ballSpeedY = 6
                elif idx <=75 and idx <80:
                    ballSpeedY = 7
                elif idx <=80:
                    ballSpeedY = 8
                #print(f'{bploop},{ballPos[1]}')
                break
    if ballPos[0] <= 20 and ballSpeedX<0:
        player2Score += 1
        ballPos = [400,300]
        textsurface = myfont.render(f'{playerScore} - {player2Score}', False, (255,255,255))
    elif ballPos[0] >= 780 and ballSpeedX>0:
        playerScore += 1
        ballPos = [400,300]
        textsurface = myfont.render(f'{playerScore} - {player2Score}', False, (255,255,255))
    ballPos[0] += ballSpeedX
    ballPos[1] += ballSpeedY
    #check if off the screen
    if victory == False:
           #s playery = y-40
        gameDisplay.fill((0,0,0))
        pygame.draw.rect(gameDisplay, (255,255,255), (pygame.Rect(playerx, playery,20,80)))
        pygame.draw.rect(gameDisplay, (255,255,255), (pygame.Rect(player2x, player2y,20,80)))
        player2HitBox = []
        playerHitBox = []
        for hitboxx in range(80):
            player2HitBox.append(hitboxx+player2y)
        for hitboxy in range(80):
            playerHitBox.append(hitboxy+playery)
        pygame.draw.line(gameDisplay, (255,255,255), (400,0),(400,600))
        
        pygame.draw.circle(gameDisplay, (255,255,255), ballPos, 7)
    
    gameDisplay.blit(textsurface,(368,0))
         # --- end draw ---
        #print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()