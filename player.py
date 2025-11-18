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
        self.score_sound=pygame.mixer.Sound('assets/Bonus/sfx_zap.ogg')
        self.shoot_sound=pygame.mixer.Sound('assets/Bonus/sfx_laser1.ogg')
        self.laser_group=pygame.sprite.Group()
        
    def update(self): 
        #want to fix so that player only moves when key is held down, 
        #when key is lifted player stops so transition between moving directions is smoother
        self.laser_group.update()
        self.x+=self.vx
        self.y+=self.vy
        self.rect.center=(self.x,self.y)
        if self.rect.right<0:
            self.x=WIDTH
        if self.rect.left>WIDTH:
            self.x=0

    def check_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.vx += -3
            if event.key == pygame.K_d:
                self.vx += 3
            if event.key ==pygame.K_SPACE:
               new_laser = Laser(self.rect.midtop)
               new_laser.shoot()
               print('shooting')
   
    def draw(self, screen):
        screen.blit(self.image,self.rect)
        #blitting lasers
        self.laser_group.draw(screen)
        for s in self.laser_group:
            s.draw(screen)

class Laser(pygame.sprite.Sprite):
    def __init__(self,coords):
        pygame.sprite.Sprite.__init__(self)
        self.x=coords[0]
        self.y=coords[1]
        self.image=pygame.image.load('assets/SS_Parts/Lasers/laserBlue01.png')
        self.image=pygame.transform.rotozoom(self.image,0,2)
        self.rect=self.image.get_rect()
        self.rect.center=(coords)
        self.sceen=screen
        self.laser_vy=8
        self.shoot_sound=pygame.mixer.Sound('assets/Bonus/sfx_laser1.ogg')
        self.laser_group=pygame.sprite.Group()
        #self.laser_group

    def update(self):
        self.y-=self.laser_vy
        self.rect.center=(self.x, self.y)
        if self.y < HEIGHT:
            self.kill()

    def shoot(self):
        new_laser=Laser(self.rect.midtop)
        self.laser_group.add(new_laser)
        self.shoot_sound.play()
        #print('shooting')
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        #bltting lasers?
        
       
        

 

   
        
