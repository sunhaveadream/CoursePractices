#alien_invasion
#2022/10/9
#author:linxu
'''
这里是游戏的整体逻辑
'''

import pygame
import sys
from settings import Settings
from ship import Ship_display

class AlienGame:
    def __init__(self):
        #pygame初始化
        pygame.init()
        self.settings=Settings()

        #设置窗口大小，设置窗口大小可调整
        self.screen=pygame.display.set_mode((self.settings.window_length,self.settings.window_width),self.settings.window_flag)
        self.bg=self.screen.image.load(self.settings.window_bg_path)
        self.screen.blit(self.bg.screen.blit(self.bg),(0,0))
        #设置窗口标题旁边的图标
        img = pygame.image.load(self.settings.window_ico_path)
        pygame.display.set_icon(img)

        #设置窗口标题
        pygame.display.set_caption(self.settings.window_name)

        #设置背景颜色
        self.bg_color=self.settings.window_bg_color
        # self.bg_photo=self.image.load(self.settings.window_bg_path)
        # self.screen.blit(self.ship_photo.screen.blit(self.bg_photo),(0,0))

        self.ship_display = Ship_display()

    #设置游戏循环，使得窗口可以一直显示
    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.ship_display.display_ship()

            #填充窗口颜色
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
        agame = AlienGame()
        agame.runGame()


