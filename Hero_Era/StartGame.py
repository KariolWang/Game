#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game
from Hero_Era.Controller import MenuInterFace as mI


"""
《君临乱世》游戏控制类、运行类
主要负责游戏逻辑实现
    * class_name:
        Run：运行游戏
    * methods：
        run： 运行游戏
"""


class Run(object):

    def __init__(self):
        """
        类初始化
            is_fill： 游戏窗口全屏开关，默认关闭全屏
        """
        self.is_fill = False

    def run(self):
        """
        游戏运行方法，主要负责游戏运行调用
            index： 游戏菜单界面对象
            is_click： 鼠标点击事件监测开关
            x，y： 鼠标当前坐标
            choice：监测点击的菜单内容
        :return: None
        """
        # 返回游戏菜单界面对象
        index = mI.MenuFace(self.is_fill)
        # 播放菜单界面背影音乐
        index.play_music()
        while True:
            # 初始化鼠标点击监测开关
            is_click = False
            # 获取鼠标当前坐标
            x, y = game.mouse.get_pos()
            # pygame全局事件监测
            for event in game.event.get():
                # 关闭窗口，退出游戏
                if event.type == game.QUIT:
                    exit(0)
                # 鼠标点击，鼠标点击事件监测开关打开
                if event.type == game.MOUSEBUTTONDOWN:
                    is_click = True
            # 获取返回的菜单点击内容
            choice = index.menu_click(x, y, is_click)
            # 根据点击内容的不同，分别进行不同的处理
            if choice == 1:
                print('初临乱世')
                pass
            elif choice == 2:
                print('乱世再起')
                pass
            elif choice == 3:
                print('退隐山林')
                exit()
            # 刷新图像
            game.display.flip()
            # 重绘窗口
            game.display.update()


if __name__ == '__main__':
    # 启动游戏
    Run().run()
