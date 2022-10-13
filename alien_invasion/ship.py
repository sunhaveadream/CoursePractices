#ship.py
#2022/10/13
#author:linxu
'''
这是飞船的部分
'''
from settings import Settings

class Ship_display:
    def __init__(self):
        self.settings=Settings()
        self.ship_photo_path=self.settings.window_ship_path
        self.ship_photo=self.image.load(self.settings.window_ship_path)
        self.ship_photo.get_rect()



    def display_ship(self):
        self.ship_photo.blit(self.bg),(300,600)