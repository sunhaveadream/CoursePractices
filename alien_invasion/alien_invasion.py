#alien_invasion
#2022/10/9
#author:linxu
'''
这里是游戏的整体逻辑
'''
#导入所需的类
import pygame
import sys
from settings import Settings
from ship import Ship_display

class AlienGame:
    def __init__(self):
        #pygame初始化
        pygame.init()

        #实例化Setting类
        self.settings=Settings()

        #设置窗口大小，设置窗口大小可调整
        self.screen=pygame.display.set_mode((self.settings.window_length,self.settings.window_width),self.settings.window_flag)

        #设置窗口标题旁边的图标
        img = pygame.image.load(self.settings.window_ico_path)
        pygame.display.set_icon(img)

        #设置窗口标题
        pygame.display.set_caption(self.settings.window_name)

        #设置背景颜色
        self.bg_color=self.settings.window_bg_color

        #设置背景图片
        self.bg_photo=pygame.image.load(self.settings.window_bg_path)
        self.bg_rect=self.bg_photo.get_rect()

        #实例化飞船类
        self.ship_display = Ship_display(self.screen)
    def keyboard_press(self):
        '''
        键盘按键按压
        '''
        for event in pygame.event.get():
            #如果鼠标点击顶部关闭按钮，则退出游戏
            if event.type == pygame.QUIT:
                sys.exit()
            #如果鼠标点击上下左右方向键，往对应方向平移
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.ship_display.move_flag=True
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.y-=1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.ship_display.move_flag=True
                if self.ship_display.move_flag:
                     self.ship_display.ship_rect.y+=1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.ship_display.move_flag=True
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.x-=1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.ship_display.move_flag=True
                if self.ship_display.move_flag:
                      self.ship_display.ship_rect.x+=1.5

    def keyboard_release(self):
        '''
        键盘按键松开
        '''
        for event in pygame.event.get():
            # 如果鼠标松开上下左右方向键，往对应方向平移
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                self.ship_display.move_flag=False
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.y -= 1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.y += 1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.x -= 1.5
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if self.ship_display.move_flag:
                    self.ship_display.ship_rect.x += 1.5

    def mouse_click(self):
        '''
        鼠标点击
        '''
        pass

    def mouse_release(self):
        '''
        鼠标松开
        '''
        pass

    def mouse_move(self):
        '''
        鼠标移动
        '''
        pass

    def update_screen(self):
        '''
        更新屏幕
        '''
        # 填充窗口颜色
        self.screen.fill(self.bg_color)
        # 填充背景图片
        self.screen.blit(self.bg_photo, self.bg_rect)
        # 显示飞船
        self.ship_display.display_ship()
        # 更新屏幕内容
        # 部分更新
        # pygame.display.update()
        # 整个更新
        pygame.display.flip()

    #设置游戏循环，死循环使得窗口可以一直显示
    def runGame(self):
        while True:
            self.keyboard_press()
            self.keyboard_release()
            self.update_screen()

if __name__ == '__main__':
        agame = AlienGame()
        agame.runGame()


