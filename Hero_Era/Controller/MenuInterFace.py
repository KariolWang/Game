#! D:/Tools/Python35
from Hero_Era.View import Draw_Menu as dM

"""
菜单界面控制类
负责初始化游戏窗口及菜单界面属性，实现菜单界面的功能
    * class_name：
        MenuFace：菜单界面
    * methods：
        background：菜单界面背景内容
        play_music：菜单界面背景音乐
        menu_click：菜单点击事件
"""


class MenuFace(object):

    def __init__(self, is_fill):
        """
        类初始化
            screen_size：游戏窗口大小
            screen_title：游戏窗口标题
            background_image：菜单界面背景图
            background_music：菜单界面背景音乐
            cursor_image：鼠标图像
            title_image：游戏标题
            button_images：菜单按钮
        :param is_fill: 窗口全屏开关
        """
        self.screen_size = (1280, 720)
        self.screen_title = 'Python单机游戏-乱世君临'
        self.background_image = 'Media/images/bg.png'
        self.background_music = 'Media/music/menu.mp3'
        self.cursor_image = 'Media/images/cursor.png'
        self.title_image = 'Media/images/title.png'
        self.is_fill = is_fill
        self.button_images = [
            'Media/images/start.png',
            'Media/images/continue.png',
            'Media/images/end.png'
        ]

    def background(self):
        """
        绘制菜单背景
            menu：获取游戏窗口对象
        :return: menu
        """
        # 获取游戏窗口对象
        menu = dM.DrawIndex(self.screen_size, self.screen_title, self.background_image, self.background_music,
                            self.cursor_image, self.title_image, self.is_fill)
        # 绘制背景
        menu.background()
        # 绘制游戏标题
        menu.title()
        return menu

    def play_music(self):
        """
        播放音乐
        :return: None
        """
        self.background().music()

    def menu_click(self, x, y, is_click):
        """
        菜单点击事件
        :param x: 当前鼠标x坐标
        :param y: 当前鼠标y坐标
        :param is_click: 鼠标点击事件开关
        :return: 菜单点击内容
        """
        return self.background().click(self.button_images, x, y, is_click)
