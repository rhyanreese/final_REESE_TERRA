import pygame
from random import randint
from util_params import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

def make_background():
    #making tiled background (EXCEPT IM SPACE SO I DONT HAVE TO RAHHHHHHHHHHH)
    space_location='assets/Backgrounds_SS/blue.png'
    space_surface=pygame.image.load(space_location)

    blue_planet_location='assets/Planets/planet07.png'
    blue_planet_surface=pygame.image.load(blue_planet_location)
    blue_planet_surface=pygame.transform.rotozoom(blue_planet_surface,0,.75)

    brown_planet_location='assets/Planets/planet05.png'
    brown_planet_surface=pygame.image.load(brown_planet_location)
    brown_planet_surface=pygame.transform.rotozoom(brown_planet_surface,0,.25)

    #seaweed_a_location='assets/images/seaweed_green_a.png'
    #seaweed_tile=pygame.image.load(seaweed_a_location)

    #get tile width, height
    tile_width =space_surface.get_width()
    tile_height=space_surface.get_height()

    #make new surface background with same w,h as screen
    background=pygame.Surface((WIDTH,HEIGHT))

    #loop over the background and place tiles on it
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(space_surface,(x,y))

    #make a row of snad
    #y_sand=HEIGHT-tile_height
    #for x in range(0,WIDTH,tile_width):
        #blit the sand tile
        #background.blit(sand_top_a,(x,y_sand))

    #randomly place seaweed
    #num_seaweed=3
    #for i in range(num_seaweed):
        #x=randint(0,WIDTH)
        #y=HEIGHT-tile_height
        #blit sewaeed
        #background.blit(seaweed_tile,(x,y))
    background.blit(space_surface,(0,0))
    background.blit(brown_planet_surface,(0,0))
    background.blit(blue_planet_surface,(WIDTH//2,HEIGHT//2))
    #return backgroudn surface
    return background

#





    