import pygame
from util_params import *
from util_background import *
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH/2, y=HEIGHT*(9/10)):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.image=pygame.image.load('assets/SS_Parts/playerShip1_blue.png')
        self.image=pygame.transform.rotozoom(self.image,0,1.2)
        self.rect=self.image.get_rect()
        self.vx=0
        self.vy=0
        self.score=0

    def update(self): 
        #want to fix so that player only moves when key is held down, 
        #when key is lifted player stops so transition between moving directions is smoother
        self.x+=self.vx
        self.y+=self.vy
        self.rect.center=(self.x,self.y)

    def check_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.vx += -3
            if event.key == pygame.K_d:
                self.vx += 3
            #if event.key ==pygame.K_SPACE


    def draw(self, screen):
        screen.blit(self.image,self.rect)
        
