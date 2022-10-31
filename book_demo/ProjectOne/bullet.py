import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
    """管理从船上发射的子弹的类"""

    def __init__(self, ai_game):
        """在船的当前位置创建子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0，0）处创建子弹，然后设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 将子弹的位置存储为十进制值
        self.y = float(self.rect.y)

    def update(self):
        """在屏幕上移动子弹"""
        # 更新子弹的速度
        self.y -= self.settings.bullet_speed
        # 更新子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """把子弹画到屏幕上"""
        pygame.draw.rect(self.screen, self.color, self.rect)
