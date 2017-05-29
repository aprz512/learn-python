# -*- coding: utf-8 -*-
import pygame
from bullet import Bullet
from alien import Alien
from alien import Boss
from random import randint
from scoreboard import Scoreboard
import time

def check_events(ship_controller, stats, play_button, settings, aliens, bullets, screen, ship, sb):
    for event in pygame.event.get():
        ship_controller.detect_event(event, stats, play_button, settings, aliens, bullets, screen, ship, sb)

def creat_alien_fleet(settings, screen, aliens):
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    h_space = settings.alien_h_spacing
    v_space = settings.alien_v_spacing
    aliens_cols = int((screen.get_rect().width - settings.side_spacing * 2) / (alien_width + h_space))
    aliens_rows = int((settings.screen_height / 3) / (alien_height + v_space))

    for aliens_row in range(aliens_rows):
        # 创建第一行外星人
        for aliens_col in range(aliens_cols):
            # 创建一个外星人并将其加入当前行
            random_number = randint(-5, 10)
            if random_number > 0 :
                alien = Alien(screen, settings)
            else :
                alien = Boss(screen, settings)
            alien.x = aliens_col * (alien_width + h_space) + h_space
            alien.y = aliens_row * (alien_height + v_space) + v_space
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)

def remove_hit_aliens(bullets, aliens, settings, screen, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹， 加快游戏节奏， 并创建一群新的外星人
        bullets.empty()
        settings.increase_speed()
        creat_alien_fleet(settings, screen, aliens)
        stats.level += 1
        sb.prep_level()

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

def check_ship(settings, stats, screen, ship, aliens, bullets, sb):
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)

def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        creat_alien_fleet(settings, screen, aliens)
        ship.center_ship()
        # 暂停
        time.sleep(3)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break

def update_screen(settings, stats, screen, ship, aliens, bullets, sb):
    screen.fill(settings.screen_bg_color)

    for bullet in bullets.sprites():
        bullet.blit_self()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    for alien in aliens.sprites():
        if alien.check_edges():
            for alien in aliens.sprites():
                alien.reverse()
            break

    for alien in aliens.sprites():
        alien.blit_self()

    ship.blit_self()

    sb.show_score()

    remove_hit_aliens(bullets, aliens, settings, screen, stats, sb)

    check_ship(settings, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)

    # 刷新屏幕
    pygame.display.flip()

def update_play_button(stats, play_button):
    # 如果游戏处于非活动状态， 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 刷新屏幕
    pygame.display.flip()

def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
