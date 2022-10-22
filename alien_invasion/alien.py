#alien
#2022/10/19
#author:linxu
# help(super)
import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,on_screen):
        super().__init__()
        self.settings=Settings()
        self.screen=on_screen.screen
        self.screen_rect=self.screen.get_rect()
        self.image=pygame.image.load(self.settings.alien_path)
        self.image.set_colorkey(self.settings.window_bg_color)
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def check_edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left<=0:
            return True

    def update(self):
        self.x  += (self.settings.alien_speed*self.settings.group_direction)
        self.rect.x=self.x