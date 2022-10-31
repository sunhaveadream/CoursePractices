import pygame
 
from pygame.sprite import Sprite
 
class Ship(Sprite):
    """一个管理飞船的类"""
 
    def __init__(self, ai_game):
        """初始化飞船并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 将位置赋给一个能够存储小数值的变量
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志更新飞船位置"""
        # 更新飞船的x值，而不是矩形
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 更新self.x后，根据它来控制飞船位置的self.rect.x
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """把船放在屏幕中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
