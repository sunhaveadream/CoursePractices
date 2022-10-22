#ship.py
#2022/10/13
#author:linxu
'''
这是飞船的部分
'''
import pygame
from settings import Settings

class Ship_display:
    def __init__(self,on_screen):
        #实例化设置类
        self.settings=Settings()
        #飞船图片存放路径
        self.ship_photo_path=self.settings.window_ship_path
        #加载飞船图片
        self.ship_photo=pygame.image.load(self.ship_photo_path)
        #让飞船背景色透明
        self.ship_photo.set_colorkey(self.settings.window_bg_color)
        #获取飞船图像的位置矩形
        self.ship_rect=self.ship_photo.get_rect()
        #把形参传给类的on_screen属性
        self.on_screen=on_screen
        #获取屏幕的位置矩形
        self.rect=self.on_screen.get_rect()
        #把飞船放在屏幕的底部中间
        self.ship_rect.midbottom=self.rect.midbottom
        #初始化移动标志，初始化设置为不移动
        self.move_left_flag=False
        self.move_right_flag=False
        self.move_up_flag=False
        self.move_down_flag=False

    def display_ship(self):
        '''
        绘制飞船图片到屏幕上
        '''
        self.on_screen.blit(self.ship_photo,self.ship_rect)

    def update_ship(self):
        '''
        更新飞船位置
        '''
        if self.move_left_flag:
            if self.ship_rect.left >0:
                self.ship_rect.x -= self.settings.speed
        elif self.move_right_flag:
            if self.ship_rect.right < self.on_screen_rect.right:
                self.ship_rect.x += self.settings.speed
        elif self.move_up_flag:
            if self.ship_rect.top >0:
                self.ship_rect.y -= self.settings.speed
        elif self.move_down_flag:
            if self.ship_rect.bottom < self.on_screen_rect.bottom:
                self.ship_rect.y += self.settings.speed

