import pygame
from util_params import *
from util_background import *
from player import *
from enemy import *

pygame.init()

def make_gameover():
    go_font=pygame.font.Font('assets/Fonts/Kenney Future.ttf', 60)
    white=(246,220,172)
    go_surface=go_font.render('GAME OVER',1, white)
    go_rect=go_surface.get_rect()
    go_rect.center=(WIDTH//2, HEIGHT//2)
    black=(0,0,0)

    go_background=pygame.surface.Surface((WIDTH,HEIGHT))
    go_background.fill(black)
       
    go_background.blit(go_surface, (WIDTH//2, HEIGHT//2))

    return go_background

        
      
    
            



    



    