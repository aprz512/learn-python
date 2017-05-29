# -*- coding: utf-8 -*-
import pygame
import sys
from bullet import Bullet
from random import randint
import game_functions as gf

class KeyController(object):
    """docstring for KeyController."""
    def __init__(self, ship, bullets, settings, screen):
        super(KeyController, self).__init__()
        self.ship = ship
        self.bullets = bullets
        self.settings = settings
        self.screen = screen

        self.moving_left = False
        self.moving_right = False

    def update_ship(self):
        """ 移动飞船 """
        if self.moving_right:
            self.ship.move_right()
        elif self.moving_left:
            self.ship.move_left()

    def fire(self):
        if len(self.bullets) < self.settings.max_bullet:
            bullet = Bullet(self.settings, self.ship, self.screen)
            self.bullets.add(bullet)

    def detect_down_event(self, event):
        """ 检测按键按下事件 """
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire()
        elif event.key == pygame.K_q:
            sys.exit()

    def detect_up_event(self, event):
        """ 检测按键抬起事件 """
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False

    def detect_event(self, event, stats, play_button, settings, aliens, bullets, screen, ship, sb):
        """ 检测事件 """
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            self.detect_up_event(event)
        elif event.type == pygame.KEYDOWN:
            self.detect_down_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.check_play_button(stats, play_button, mouse_x, mouse_y, settings, aliens, bullets, screen, ship, sb)

    def check_play_button(self, stats, play_button, mouse_x, mouse_y, settings, aliens, bullets, screen, ship, sb):
        """在玩家单击Play按钮时开始新游戏"""
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            stats.game_active = True
            stats.reset_stats()
            aliens.empty()
            bullets.empty()
            gf.creat_alien_fleet(settings, screen, aliens)
            ship.center_ship()
            if stats.game_active:
                # 隐藏光标
                pygame.mouse.set_visible(False)
        if button_clicked and not stats.game_active:
            # 重置游戏设置
            settings.initialize_dynamic_settings()
            stats.reset_stats()
            stats.game_active = True
            # 重置记分牌图像
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()
            # 清空外星人列表和子弹列表
            aliens.empty()
            bullets.empty()
