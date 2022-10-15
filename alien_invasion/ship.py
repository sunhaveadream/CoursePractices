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
        self.on_screen_rect=self.on_screen.get_rect()
        #把飞船放在屏幕的底部中间
        self.ship_rect.midbottom=self.on_screen_rect.midbottom
        self.move_flag=False
        # self.ship_speed=self.settings.speed

    def display_ship(self):
        '''
        绘制飞船图片到屏幕上
        '''
        self.on_screen.blit(self.ship_photo,self.ship_rect)

    # def update_ship(self,ship_speed):
    #     '''
    #     更新飞船位置
    #     '''
    #     self.ship_rect.x += ship_speed
