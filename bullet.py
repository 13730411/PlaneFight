import pygame

from pygame.sprite import Sprite
class Bullet(Sprite):
    # 这是一个对飞船发射子弹的类
    def __init__(self,setting,screen,ship):
        super().__init__()
        self.screen = screen
        self.speed = setting.bullet_speed_factor
        self.width = setting.bullet_width
        self.height = setting.bullet_height
        self.color = setting.bullet_color
        self.bullet_rect = pygame.Rect(0,0,self.width,self.height)
        # self.bullet_rect.fill(self.color),在绘制子弹的时候实现
        self.bullet_rect.centerx = ship.ship_image_rect.centerx
        self.bullet_rect.top = ship.ship_image_rect.top
        self.y = float(self.bullet_rect.y)
    # 更新子弹位置
    def update(self):
        self.y -= self.speed
        self.bullet_rect.y = self.y
    # 一切准备妥当后，开始完成子弹绘制
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.bullet_rect)