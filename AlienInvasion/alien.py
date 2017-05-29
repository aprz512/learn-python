# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """docstring for Alien."""
    def __init__(self, screen, settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('image\\black_alien_ship.png')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.speed = self.settings.alien_speed_factor

        self.y = float(self.rect.y)
        self.v_speed = self.settings.alien_v_speed_factor

    def check_edges(self):
        if self.rect.right > self.screen_rect.right:
            return True
        elif self.rect.left < self.screen_rect.left :
            return True
        else:
            return False

    def blit_self(self):
        """在指定位置绘制外星人"""
        self.x += self.speed
        self.rect.x = self.x
        self.screen.blit(self.image, self.rect)

    def reverse(self):
        """反向"""
        self.speed = -self.speed
        self.y += self.v_speed
        self.rect.y = self.y


class Boss(Alien):
    def __init__(self, screen, settings):
        super(Boss, self).__init__(screen, settings)
        self.image = pygame.image.load('image\\red_alien_ship.png')
