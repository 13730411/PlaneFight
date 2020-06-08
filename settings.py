# 建立一个类，用于存放该项目的所有配置，有利于后期项目的重构和维护
class Settings:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.bgcolor = (230,230,230)
        self.ship_move_speed = 1.5
# 设置子弹的属性
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        