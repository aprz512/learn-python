# -*- coding: utf-8 -*-
class Settings(object):
    """用于存储游戏设置的类"""

    def __init__(self):
        super(Settings, self).__init__()
        # 屏幕设置
        self.screen_width = 1024
        self.screen_height = 576
        self.screen_bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 0.3
        self.ship_limit = 2

        # 子弹设置
        self.bullet_speed_factor = 0.3
        self.max_bullet = 3

        # 外星人设置
        self.alien_speed_factor = 0.2
        self.alien_v_speed_factor = 90
        self.side_spacing = 200
        self.alien_h_spacing = 50
        self.alien_v_spacing = 30
        self.alien_points = 50

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.3
        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
