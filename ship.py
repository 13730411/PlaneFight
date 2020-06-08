# 设置一个飞船类,飞船中需要导入图片，因此需要pygame模块
import pygame
from settings import Settings
class Ship:
    def __init__(self,screen):
        self.screen = screen
        self.ship_image = pygame.image.load("images//me1.png")
        self.ship_image_rect = self.ship_image.get_rect()
        screen_rect = screen.get_rect()
        self.ship_image_rect.centerx = screen_rect.centerx
        self.ship_image_rect.bottom = screen_rect.bottom
# 将飞船显示在窗口中
    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_image_rect)




