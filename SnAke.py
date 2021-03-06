
import pygame
import sys
import time
import random

pygame.init()
'''

write:
    myfont = pygame.font.SysFont("Arial Black", 15)
    label = myfont.render("LOL", 1, (20, 230, 47))
    screen.blit(label, (100, 100))
'''
#height = altezza
#width = larghezza


FPS = 20
display_width = 1000
display_height = 1000
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 255)
base_color = (24, 56, 48)
character_color = (219, 32, 65)
enemy_color = (48, 100, 230)
gameExit = False
direction = None


block_size = 10
enemy_size = 10

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
title = pygame.display.set_caption("snake")
font = pygame.font.SysFont(None, 30)

song = pygame.mixer.music.load("Pokemon_Oro.wav")

def player(snakeList):
    for XnY in snakeList:
        pygame.draw.rect(screen, character_color, (XnY[0], XnY[1], block_size, block_size))

def textObjects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def messageToScreen(msg, color, margine_y = 0):
    textSurface, textRectangle = textObjects(msg, color)
    textRectangle.center = (display_width/2), (display_height/2) + margine_y
    screen.blit(textSurface, textRectangle)

    '''text = font.render(msg, True, color)
    screen.blit(text, (display_width/2-235, display_height/2))'''

def home():
    intro = True

    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
        
        screen.fill(base_color)
        messageToScreen("Welcome in Snake", character_color, -100)
        messageToScreen("Eat the blue squares: not Yourself!", character_color, -50)
        messageToScreen("Comands = WASD", character_color, 0)
        messageToScreen("press S for ssstart", character_color, 50)
        pygame.display.update()
        clock.tick(FPS)


        

def gameLoop():

    pygame.mixer.music.stop()
    pygame.mixer.music.play()

    gameExit = False
    gameOver = False
    direction = None

    direction_portal_w = False
    direction_portal_h = False

    main_x = display_width / 2
    main_y = display_height / 2

    main_x_change = 0
    main_y_change = 0

    snakeList = []
    snakeLenght = 1

    FPS = 20

    randEnemyx = round(random.randrange(0, display_width - enemy_size) / block_size) * block_size
    randEnemyy = round(random.randrange(0, display_height - enemy_size) / block_size) * block_size

    while not gameExit:
        while gameOver == True:
            screen.fill(base_color)
            messageToScreen("GAME OVER press R to restart the game ", character_color, -50)
            messageToScreen("or press Q for quit", character_color, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_r:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
            	if direction == None:
	                if event.key == pygame.K_LEFT:
	                    main_x_change = -block_size
	                    main_y_change = 0
	                    direction = 1
	                elif event.key == pygame.K_RIGHT:
	                    main_x_change = block_size
	                    main_y_change = 0
	                    direction = 1
	                elif event.key == pygame.K_UP:
	                    main_y_change = -block_size
	                    main_x_change = 0
	                    direction = 2
	                elif event.key == pygame.K_DOWN:
	                    main_y_change = block_size
	                    main_x_change = 0
	                    direction = 2
            if event.type == pygame.KEYDOWN:
                if direction == 1:
                    if event.key == pygame.K_UP:
                        main_y_change = -block_size
                        main_x_change = 0
                        direction = 2
                    elif event.key == pygame.K_DOWN:
                        main_y_change = block_size
                        main_x_change = 0
                        direction = 2
                elif direction == 2:
                    if event.key == pygame.K_LEFT:
                        main_x_change = -block_size
                        main_y_change = 0
                        direction = 1
                    elif event.key == pygame.K_RIGHT:
                        main_x_change = block_size
                        main_y_change = 0
                        direction = 1
                if event.key == pygame.K_f:
                        snakeLenght += 1
                        FPS += 3
                
                '''elif event.key == pygame.K_l:
                    randEnemyx = round(random.randrange(0, display_width - enemy_size ) / block_size) * block_size
                    randEnemyy = round(random.randrange(0, display_height - enemy_size) / block_size) * block_size
                    snakeLenght += 1'''

            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    main_x_change = 0
                    main_y_change = 0'''

        if main_x == display_width:
            if direction == 2:
                prec_main_y_change = main_y_change
                direction_portal_w = True
        
            main_x = -block_size
            main_x_change = block_size
            main_y_change = 0
            direction = 1

        elif main_x < 0:
            if direction == 2:
                prec_main_y_change = main_y_change
                direction_portal_w = True
                
            main_x = display_width
            main_x_change = -block_size
            main_y_change = 0
            direction = 1
            
        elif main_y == display_height:
            if direction == 1:
                prec_main_x_change = main_x_change
                direction_portal_h = True
                
            main_y = -block_size
            main_y_change = block_size
            main_x_change = 0
            direction = 2

        elif main_y < 0:
            if direction == 1:
                prec_main_x_change = main_x_change
                direction_portal_h = True

            main_y = display_height
            main_y_change = -block_size
            main_x_change = 0
            direction = 2

        if direction_portal_w == True: 
            if main_x == 0 or main_x == display_width - block_size:
                main_y_change = prec_main_y_change
                main_x_change = 0
                direction = 2
                direction_portal_w = False
            
        if direction_portal_h:
            if main_y == 0 or main_y == display_height - block_size:
                main_x_change = prec_main_x_change
                main_y_change = 0
                direction = 1
                direction_portal_h = False
        main_x += main_x_change
        main_y += main_y_change
        screen.fill(base_color)
        pygame.draw.rect(screen, enemy_color, (randEnemyx, randEnemyy, enemy_size, enemy_size))

        head = []
        head.append(main_x)
        head.append(main_y)
        snakeList.append(head)

        if len(snakeList) > snakeLenght:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == head:
                gameOver = True

        player(snakeList)
        pygame.display.update()

        #se nemico e serpente sono uguali
        if main_x == randEnemyx and main_y == randEnemyy:
            randEnemyx = round(random.randrange(0, display_width - enemy_size ) / block_size) * block_size
            randEnemyy = round(random.randrange(0, display_height - enemy_size) / block_size) * block_size
            snakeLenght += 1
            FPS += 3

        if main_y and main_y == player:
            gameOver = True

        #collision detection ( se il nemico è più grande del serpente   )
        '''if main_x > randEnemyx and main_x < randEnemyx + enemy_size or main_x + block_size > randEnemyx and \
            main_x + block_size < randEnemyx + enemy_size:

            if main_y > randEnemyy and main_y < randEnemyy + enemy_size or main_y + block_size > randEnemyy and \
                main_y + block_size < randEnemyy + enemy_size:

                randEnemyx = round(random.randrange(0, display_width - enemy_size) / block_size ) * block_size
                randEnemyy = round(random.randrange(0, display_height - enemy_size) / block_size ) * block_size
                snakeLenght += 1

            elif main_y + block_size > randEnemyy and main_y < randEnemyy + enemy_size:
                randEnemyx = round(random.randrange(0, display_width - enemy_size) / block_size ) * block_size
                randEnemyy = round(random.randrange(0, display_height - enemy_size) / block_size ) * block_size
                snakeLenght += 1 '''



        clock.tick(FPS)


    '''messageToScreen("GAME OVER", character_color)
    pygame.display.update()
    time.sleep(1)'''

    pygame.quit()
    quit()

home()
gameLoop()