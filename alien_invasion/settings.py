#setting
#2022/10/13
#author:linxu
'''
这里是游戏的设置
'''
import  pygame

class Settings:
    def __init__(self):
        self.window_length=600
        self.window_width=600
        self.window_flag=pygame.RESIZABLE
        self.window_ico_path="D:\\alien_relevent\\tubiao.ico"
        self.window_name="飞船大战外星人游戏"
        self.window_bg_color=(230,230,230)
        self.window_ship_path="D:\\alien_relevent\\ship.bmp"
        self.window_bg_path ="D:\\alien_relevent\\bg.jpg"