# 设置一个飞船类,飞船中需要导入图片，因此需要pygame模块
import pygame
from settings import Settings
class Ship:
    def __init__(self,screen,setting):
        self.screen = screen
        self.ship_setting = setting
        self.ship_image = pygame.image.load("images//me1.png")
        self.ship_image_rect = self.ship_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ship_image_rect.centerx = self.screen_rect.centerx
        self.ship_image_rect.bottom = self.screen_rect.bottom
        self.move_right_flag = False
        self.move_left_flag = False
        self.move_up_flag = False
        self.move_down_flag = False
        self.ship_center = float(self.ship_image_rect.centerx)
        self.ship_bottom = float(self.ship_image_rect.bottom)
# 将飞船显示在窗口中
    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_image_rect)
# 管理飞船位置
    def update(self):
        if self.move_right_flag and (self.ship_image_rect.right < self.screen_rect.right):
            self.ship_center += self.ship_setting.ship_move_speed
        if self.move_left_flag and (self.ship_image_rect.left > 0):
            self.ship_center -= self.ship_setting.ship_move_speed
        if self.move_up_flag and (self.ship_image_rect.bottom > 0):
            self.ship_bottom -= self.ship_setting.ship_move_speed
        if self.move_down_flag and (self.ship_image_rect.bottom < self.screen_rect.bottom):
            self.ship_bottom += self.ship_setting.ship_move_speed
        self.ship_image_rect.bottom = self.ship_bottom
        self.ship_image_rect.centerx = self.ship_center