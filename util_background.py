import pygame
from random import randint
from util_params import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

def make_background():
    #making tiled background (EXCEPT IM SPACE SO I DONT HAVE TO RAHHHHHHHHHHH)
    space_location='Backgrounds_SS/blue.png'
    space_surface=pygame.image.load(space_location)

    #sand_top_a_location='assets/images/terrain_sand_top_a.png'
    #sand_top_a=pygame.image.load(sand_top_a_location)

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
    #return backgroudn surface
    return background

#





    