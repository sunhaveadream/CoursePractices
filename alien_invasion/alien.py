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
        self.screen=on_screen.screen
        self.alien_photo=pygame.image.load("D:\\alien_relevent\\alien.bmp")
        self.alien_rect=self.alien_photo.get_rect()
        self.alien_rect.x=self.alien_rect.width
        self.alien_rect.y=self.alien_rect.height
        self.x=float(self.alien_rect.x)

    def alien_draw(self):
        self.on_screen.blit(self,self.alien_photo,self.alien_rect)
