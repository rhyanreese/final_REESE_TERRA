import pygame
from random import randint
from util_params import *
from util_background import *
from player import *
from enemy import Enemy
from score import *
from screens import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

######## TEST ZONE ########


#############################
title=Terra_text()
player=Player() 
background = make_background()
go_background=make_gameover()

#new_laser=Laser(player.rect.midtop)

enemy_group=pygame.sprite.Group()
for i in range(10):
    enemy_group.add(Enemy(randint(0,WIDTH),100))

#laser_group=pygame.sprite.Group()
#laser_group.add(new_laser)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.check_event(event)
          
    #make background + update assets
    screen.blit(background,(0,0))
    player.update()
    enemy_group.update()
    #laser_group.update()
    title.update()
    #title.update_score(player.score)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            screen.blit(go_background, (WIDTH//2, HEIGHT//2))
            print('gameover')
   

    #draw game
    title.draw(screen)
    # put in characters
    player.draw(screen)
    #laser_group.draw(screen)
    enemy_group.draw(screen)   


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 