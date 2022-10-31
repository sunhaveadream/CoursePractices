class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色
        self.bg_color = (230, 230, 230)
        # 设置窗口标题的图标存放路径
        self.window_ico_path="images/tubiao.ico"
        # 设置窗口背景图片存放路径
        self.window_bg_path ="images/bg1.jpg"

        # 飞船的设置
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 215, 0)
        self.bullets_allowed = 3

        # 外星人的设置
        self.fleet_drop_speed = 10

        # 游戏的速度
        self.speedup_scale = 1.1
        # 外星人的点值增加
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化在整个游戏中更改的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction为1表示右，-1表示左侧
        self.fleet_direction = 1

        # 外星人价值得分
        self.alien_points = 50

    def increase_speed(self):
        """增加速度设置和外星人点值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
