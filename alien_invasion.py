'''
1、使用python开始开发一个2D游戏，就是外星人入侵游戏，这个游戏主要使用的是pygame模块,
首先是在python 中安装pygame模块，安装pygame的方法，在linux和windows上面， 基本都
差不多。首先安装pip模块，pip模块，有点类似linux中的rpm，即python的包管理软件，通过
pip或pip3（主要考虑python版本的问题），安装pygame。安装完pygame，就可以通过pycharm
开发2D游戏了。
'''
'''
2、窗口简单的显示功能是完成了，但是有个问题，就是现在所有的配置都在一个函数里面，所以如果后期程序
变大，那么后期的修改和维护就会变得很困难，并且也不符合面向对象编程的思想。python中一切皆对象。
所以基于这个原因，我们现在需要建立一个设置类Settings，python中类名和文件名不同于java要求必须一致。
所以，一般文件名用小写，而类名用大写
'''
'''
3、现在已经完成了窗口显示，并且也进行了面向对象设置。下一步就是开始飞船类设计以及飞船在窗口的显示了，
先设计一个飞船类Ship
'''
"""
4、经过上面3个步骤，已经可以实现一辆飞船停在光秃秃的窗口上，但是现在还需要对代码进行重构
简化主函数，将飞船的一些功能封装到其他的模块中。
"""
# 开发游戏第一部，首先导入相应的包，比如pygame，sys等
# 导入pygame模块
import pygame
# 导入设置模块
from settings import Settings
# 导入飞船类
from ship import Ship
# 定义一个窗口函数，可以显示一个主窗口
import game_function as gf
def run_game():
    # 首先pygame初始化
    pygame.init()
    av_setting = Settings()
    # 设置pygame窗口模式以及值
    screen = pygame.display.set_mode((av_setting.width,av_setting.height))
    pygame.display.set_caption("外星人入侵游戏...")
    my_ship = Ship(screen,av_setting)
    # 使用一个死循环，开始刷新显示屏幕
    while True:
        # 在一个死循环中，一定要设置一个中断条件，从而可以在某种情况下，跳出循环。本程序就是通过pygame的
        # 退出事件，中断这个死循环
        # 下面的事件代码，通过game_function模块取代
        # for event in pygame.event.get():
        # 事件类型与pygame的QUIT一致，则退出显示窗口
        # if event.type == pygame.QUIT:
        #    sys.exit()
        gf.check_events(my_ship)
        my_ship.update()
        gf.update_screen(av_setting,screen,my_ship)
run_game()

