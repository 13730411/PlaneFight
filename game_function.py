# 本模块主要功能是实现飞船中使用的绝大部分函数的封装
import pygame
import sys
from bullet import Bullet
def check_events(ship,setting,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,setting,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def check_keydown_events(event,ship,setting,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right_flag = True
    if event.key == pygame.K_LEFT:
        ship.move_left_flag = True
    if event.key == pygame.K_UP:
        ship.move_up_flag = True
    if event.key == pygame.K_DOWN:
        ship.move_down_flag = True
    if event.key == pygame.K_SPACE:
        print(event.key)
        print("========")
        print(pygame.K_SPACE)
        bullet = Bullet(setting,screen,ship)
        bullets.add(bullet)
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right_flag = False
    if event.key == pygame.K_LEFT:
        ship.move_left_flag = False
    if event.key == pygame.K_UP:
        ship.move_up_flag = False
    if event.key == pygame.K_DOWN:
        ship.move_down_flag = False
def update_screen(av_setting,screen,ship,bullets):
    for bul in bullets.sprites():
        bul.draw_bullet()
        print("update bullet")
    screen.fill(av_setting.bgcolor)
    ship.blitme()
    pygame.display.flip()
