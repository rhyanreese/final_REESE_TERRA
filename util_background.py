import pygame
from random import randint
from util_params import *
from random import choice

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

def make_background():
    #making background 
    space_location='assets/Backgrounds_SS/blue.png'
    space_surface=pygame.image.load(space_location)

    #planets info
    blue_planet_location='assets/Planets/planet07.png'
    blue_planet_surface=pygame.image.load(blue_planet_location)
    blue_planet_surface=pygame.transform.rotozoom(blue_planet_surface,0,.75)

    brown_planet_location='assets/Planets/planet05.png'
    brown_planet_surface=pygame.image.load(brown_planet_location)
    brown_planet_surface=pygame.transform.rotozoom(brown_planet_surface,0,.25)

    #extra stars
    star_assets=['assets/SS_Parts/Effects/star1.png', 
                 'assets/SS_Parts/Effects/star2.png', 
                 'assets/SS_Parts/Effects/star3.png']
    star_surface=pygame.image.load(choice(star_assets))
    star_surface=pygame.transform.rotozoom(star_surface,0,.35)

    #get tile width, height
    tile_width = space_surface.get_width()
    tile_height = space_surface.get_height()

    #make new surface background with same w,h as screen
    background=pygame.Surface((WIDTH,HEIGHT))

    #loop over the background and place tiles on it
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(space_surface,(x,y))
    
    #randomly place stars
    num_stars=40
    for i in range(num_stars):
        x=randint(0,WIDTH)
        y=randint(0,HEIGHT)
        #blit sewaeed
        background.blit(star_surface,(x,y))

    background.blit(space_surface,(0,0))
    background.blit(brown_planet_surface,(0,0))
    background.blit(blue_planet_surface,(WIDTH//2,HEIGHT//2))
    #return background surface
    return background

#





    