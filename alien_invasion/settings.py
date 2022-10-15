#setting
#2022/10/13
#author:linxu
'''
这里是游戏的设置
'''
import  pygame

class Settings:
    def __init__(self):
        #设置窗口长度
        self.window_length=600
        #设置窗口宽度
        self.window_width=600
        #设置窗口可调节大小
        self.window_flag=pygame.RESIZABLE
        #设置窗口标题的图标存放路径
        self.window_ico_path="D:\\alien_relevent\\tubiao.ico"
        #设置窗口名字
        self.window_name="飞船大战外星人游戏"
        #设置窗口背景色
        self.window_bg_color=(230,230,230)
        #设置飞船图片存放路径
        self.window_ship_path="D:\\alien_relevent\\ship.bmp"
        #设置窗口背景图片存放路径
        self.window_bg_path ="D:\\alien_relevent\\bg.jpg"
        # #设置速度
        # self.speed=1.5