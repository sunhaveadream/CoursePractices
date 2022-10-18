#bullet
#2022/10/16
#author:linxu
import pygame
from settings import Settings
from ship import Ship_display
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,on_screen):
        super().__init__()
        self.screen=on_screen.screen
        self.settings=on_screen.settings
        self.colour=self.settings.bullet_colour
        self.bullet_rect = pygame.Rect(self.settings.bullet_left,self.settings.bullet_top,self.settings.bullet_width,self.settings.bullet_height)
        self.bullet_rect.midtop = on_screen.ship_display.ship_rect.midtop
        self.y=float(self.bullet_rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.bullet_rect.y=self.y

    def bullet_draw(self):
        pygame.draw.rect(self.screen, self.colour, self.bullet_rect)

