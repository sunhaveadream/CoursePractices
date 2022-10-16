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
        #设置窗口背景图片存放路径
        self.window_bg_path ="D:\\alien_relevent\\bg.jpg"
        #设置飞船图片存放路径
        self.window_ship_path="D:\\alien_relevent\\ship.bmp"
        #设置飞船的移动速度
        self.speed=1
        #设置子弹的矩形的纵横
        self.bullet_left = 0
        self.bullet_top=0
        self.bullet_width=15
        self.bullet_height=15
        self.bullet_position=(self.bullet_left,self.bullet_top,self.bullet_width,self.bullet_height)
        #设置子弹颜色
        self.bullet_colour=(0, 0, 255)
        #设置子弹的速度
        self.bullet_speed=1
        #设置子弹矩形的边框大小(0表示填充矩形)
        self.bullet_frame=20
