# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
from key_controller import KeyController
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_status import GameStats
from button import Button
from scoreboard import Scoreboard

def start_game():

    # 游戏名字和设置
    game_title = "Alien Invasion"
    game_settings = Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_title)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    # 创建玩家飞船
    ship = Ship(screen, game_settings)

    # 创建用于储存子弹的编组
    bullets = Group()

    # 创建用于储存外星人的编组
    aliens = Group()
    gf.creat_alien_fleet(game_settings, screen, aliens)

    # 按键控制器
    key_controller = KeyController(ship, bullets, game_settings, screen)

    # 创建Play按钮
    play_button = Button(game_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        gf.check_events(key_controller, stats, play_button, game_settings, aliens, bullets, screen, ship, sb)
        if stats.game_active:
            key_controller.update_ship()
            gf.update_screen(game_settings, stats, screen, ship, aliens, bullets, sb)
        else:
            gf.update_play_button(stats, play_button)

start_game()
