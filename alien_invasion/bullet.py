#bullet
#2022/10/16
#author:linxu
import pygame
import sys
from settings import Settings
from ship import Ship_display
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,display_screen):
        super().__init__()
        self.screen=self.display_screen.screen
        self.colour=self.settings.bullet_colour
        self.bullet_rect = pygame.Rect(self.settings.bullet_left,self.settings.bullet_top,self.settings.bullet_width,self.settings.bullet_height)
        self.bullet_rect.midtop=self.Ship_display.ship_rect.midtop
        self.y=float(self.bullet_rect.y)

    def bullet_update(self):
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y

    def bullet_update(self):
        pygame.draw.rect(self.display_screen, self.colour, self.bullet_rect)

