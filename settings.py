# 建立一个类，用于存放该项目的所有配置，有利于后期项目的重构和维护
class Settings:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.bgcolor = (230,230,230)

