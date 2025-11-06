import pygame
from util_params import *
from util_background import *
from player import *

class Terra_text():
    def __init__(self):
        self.title_font=pygame.font.Font('assets/Fonts/Kenney Future.ttf', 70)
        self.white=(246,220,172)
        self.title_surface =self.title_font.render('Terra Defender',1, self.white)
        self.title_rect=self.title_surface.get_rect()
        self.title_rect.center=(WIDTH//2, HEIGHT//2)
        self.birth_time=pygame.time.get_ticks()
        self.death_time=2000

        self.score_font=pygame.font.Font('assets/Fonts/Kenney Future Narrow.ttf',40)
        self.white=(246,220,172)
        self.score_surface=self.score_font.render('0',1,self.white)

    def update_score(self,score):
        self.score_surface=self.score_surface.render(f"{score}",1,self.white)

    def update(self):
        current_age=pygame.time.get_ticks() - self.birth_time
        current_age_percent=current_age/self.death_time
        self.title_surface.set_alpha(225-current_age_percent * 255)

    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.score_surface, (20,20))


