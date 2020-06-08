# 本模块主要功能是实现飞船中使用的绝大部分函数的封装
import pygame
import sys
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()