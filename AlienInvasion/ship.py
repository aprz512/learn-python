# -*- coding: utf-8 -*-
import pygame
import os
from pygame.sprite import Sprite

class Ship(Sprite):
    """玩家控制的宇宙飞船类"""

    def __init__(self, screen, settings):
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("image\\rocket.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)

    def blit_self(self):
        self.screen.blit(self.image, self.rect)

    def move_left(self):
        if (self.rect.left > self.screen_rect.left):
            self.centerx -= self.settings.ship_speed_factor
            self.rect.centerx = self.centerx

    def move_right(self):
        if (self.rect.right < self.screen_rect.right):
            self.centerx += self.settings.ship_speed_factor
            self.rect.centerx = self.centerx

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
