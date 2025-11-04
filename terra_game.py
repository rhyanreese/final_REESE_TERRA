import pygame
from random import randint
from util_params import *
from util_background import *
from player import Player
from enemy import Enemy

# pygame setup
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

######## TEST ZONE ########

#make a tiled background
player=Player()
enemy=Enemy()
#############################
background = make_background()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.check_event(event)
    
    player.update()

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    screen.blit(background,(0,0))
    # RENDER YOUR GAME HERE
    player.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()