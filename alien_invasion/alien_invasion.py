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
from bullet import Bullet

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

        #实例化子弹类
        self.bullets=pygame.sprite.Group()

    def bullet_fire(self):
        if len(self.bullets)<self.settings.bullet_sum:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def bullet_update(self):
        self.bullets.update()

    def keyboard_action(self):
        for event in pygame.event.get():
            #如果鼠标点击顶部关闭按钮，则退出游戏
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keyboard_press(event)
            elif event.type == pygame.KEYUP:
                self.keyboard_release(event)

    def keyboard_press(self,event):
        '''
        键盘按键按压
        '''
        if event.key == pygame.K_UP:
            self.ship_display.move_up_flag=True
        elif event.key == pygame.K_DOWN:
            self.ship_display.move_down_flag=True
        elif event.key == pygame.K_LEFT:
            self.ship_display.move_left_flag=True
        elif event.key == pygame.K_RIGHT:
            self.ship_display.move_right_flag=True
        elif event.key == pygame.K_SPACE:
            self.bullet_fire()
        elif event.key == pygame.K_q:
            sys.exit()


    def keyboard_release(self,event):
        '''
        键盘按键松开
        '''
        if event.key == pygame.K_UP:
            self.ship_display.move_up_flag = False
        elif event.key == pygame.K_DOWN:
            self.ship_display.move_down_flag = False
        elif event.key == pygame.K_LEFT:
            self.ship_display.move_left_flag = False
        elif event.key == pygame.K_RIGHT:
            self.ship_display.move_right_flag = False

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
        for bullet in self.bullets.sprites():
            bullet.bullet_draw()
        # 显示飞船
        self.ship_display.display_ship()
        # 更新屏幕内容
        # 部分更新
        # pygame.display.update()
        # 整个更新
        pygame.display.flip()

    def runGame(self):
        # 设置游戏循环，死循环使得窗口可以一直显示
        while True:
            #捕获键盘事件
            self.keyboard_action()
            #更新飞船图像
            self.ship_display.update_ship()
            #更新子弹图像
            self.bullet_update()
            #更新屏幕
            self.update_screen()

if __name__ == '__main__':
        agame = AlienGame()
        agame.runGame()


