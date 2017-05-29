# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    docstring for Bullet.
    继承 Sprite 是为了方便将元素进行编组，可以同时操纵组中的所有元素
    """
    def __init__(self, settings, ship, screen):
        super(Bullet, self).__init__()
        self.settings = settings
        self.ship = ship
        self.screen = screen

        self.image = pygame.image.load("image\\bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        self.centery = float(self.rect.centery)

    def blit_self(self):
        self.screen.blit(self.image, self.rect)
        self.update()

    def update(self):
        self.centery -= self.settings.bullet_speed_factor
        self.rect.centery = self.centery
