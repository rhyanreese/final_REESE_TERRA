import pygame
from util_params import *
from util_background import *
from player import *

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('assets/SS_Parts/Lasers/laserBlue01.png')
        self.rect=self.image.get_rect()
        self.x=self.rect.midtop
        self.y=self.rect.midtop
        self.laser_vy=8

        self.shoot_sound=pygame.mixer.Sound('assets/Bonus/sfx_laser1.ogg')

    def shoot(self):
        self.x=self.rect.midtop
        self.y+=self.laser_vy