import pygame
from util_params import *
from util_background import *
from player import Player
from random import randint, choice

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=randint(0,WIDTH),y=100):
        pygame.sprite.Sprite.__init__(self)
        self.assets = ['assets/SS_Exp/Ships/spaceShips_001.png', 
                        'assets/SS_Exp/Ships/spaceShips_003.png', 
                        'assets/SS_Exp/Ships/spaceShips_008.png',
                        'assets/SS_Exp/Ships/spaceShips_009.png']
        self.fp= choice(self.assets)
        self.x=x
        self.y=y
        self.vy=.5
        self.vx=0
        self.image=pygame.image.load(self.fp)
        self.image=pygame.transform.rotozoom(self.image,0,.7)
        self.image=pygame.transform.flip(self.image,1,0)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.state='alive'
        if self.rect.bottom > HEIGHT:
            self.y = 100
    
    def update(self):
        self.y+=self.vy
        self.x+=self.vx
        self.rect.center=(self.x,self.y)

        collision=pygame.sprite.spritecollide(self,0)
        if collision:
            self.x+=10

    def draw(self,screen):
        screen.blit(self.image, self.rect)
