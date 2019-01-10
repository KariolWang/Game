#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game

"""
绘制游戏主窗口及菜单界面
    * class_name：
        DrawIndex：绘制主页
    * methods：
        music：加载音乐
        background：加载背景图
        title：加载标题及计算标题绘制坐标
        cursor：加载鼠标及计算鼠标绘制坐标
        menu：加载菜单按钮及计算菜单按钮绘制坐标
        click：菜单按钮点击判断
"""


class DrawIndex(object):
    
    def __init__(self, size, screen_title, image, music, cursor, title_image, is_fill):
        """
        类初始化
            screen_size：游戏窗口大小
            screen_title：游戏窗口标题
            background_image：背景图路径
            background_music：背影音乐路径
            cursor_image：鼠标图像路径
            title_image：游戏标题路径
            screen：初始化一个游戏窗口
        :param size: 游戏窗口大小
        :param screen_title: 游戏窗口标题
        :param image: 背景图路径
        :param music: 背景音乐路径
        :param cursor: 鼠标图像路径
        :param title_image: 游戏标题路径
        :param is_fill: 窗口全屏开关
        """
        self.screen_size = size
        self.screen_title = screen_title
        self.background_image = image
        self.background_music = music
        self.cursor_image = cursor
        self.title_image = title_image
        self.screen = game.display.set_mode(self.screen_size, game.FULLSCREEN if is_fill else 0, 32)

    def music(self):
        """
        播放背景音乐
        :return: None
        """
        # 加载背景音乐
        game.mixer_music.load(self.background_music)
        # 设置循环播放
        game.mixer_music.play(-1)

    def background(self):
        """
        绘制背景素材
            bg：加载背景图片对象
        :return: None
        """
        # 加载窗口标题
        game.display.set_caption(self.screen_title)
        # 加载背景图片
        bg = game.image.load(self.background_image)
        # 绘制背景图片到游戏窗口上
        self.screen.blit(bg, (0, 0))

    def title(self):
        """
        绘制标题图像
            title：加载标题图像
            x，y：计算标题绘制坐标
        :return: None
        """
        # 加载标题图像
        title = game.image.load(self.title_image)
        # 计算标题x坐标
        x = self.screen_size[0] / 2 - title.get_width() / 2
        # 计算标题y坐标
        y = self.screen_size[1] * 0.15 - title.get_height() / 2
        # 绘制标题到游戏窗口上
        self.screen.blit(title, (x, y))

    def cursor(self, x, y):
        """
        绘制鼠标图像
            cursor：加载鼠标图像
            x，y：计算鼠标绘制坐标
        :param x: 鼠标x坐标
        :param y: 鼠标y坐标
        :return: None
        """
        # 加载鼠标图像
        cursor = game.image.load(self.cursor_image)
        # 设置鼠标不可见
        game.mouse.set_visible(False)
        # 计算鼠标x坐标
        x -= cursor.get_width() / 2
        # 计算鼠标y坐标
        y -= cursor.get_height() / 2
        # 绘制鼠标图像到游戏窗口上
        self.screen.blit(cursor, (x, y))

    def menu(self, button, num):
        """
        绘制菜单按钮
            bt：加载菜单按钮图像
            x：计算菜单按钮x坐标
            y：计算菜单按钮y坐标
            x0：计算菜单按钮x起始坐标
            x1：计算菜单按钮x结束坐标
            y0：计算菜单按钮y起始坐标
            y1：计算菜单按钮y结束坐标
        :param button: 菜单按钮图像
        :param num: 菜单按钮的序列号
        :return: 菜单按钮的坐标范围
        """
        # 加载按钮图像
        bt = game.image.load(button)
        # 计算按钮x坐标
        x = self.screen_size[0] / 2 - bt.get_width() / 2
        # 计算按钮y坐标
        y = self.screen_size[1] * 0.12 * num - bt.get_height() / 2
        # 绘制按钮到游戏窗口
        self.screen.blit(bt, (x, y))
        # 计算按钮x起始坐标
        x0 = round(self.screen_size[0] / 2 - bt.get_width() / 2)
        # 计算按钮x结束坐标
        x1 = x0 + bt.get_width()
        # 计算按钮y起始坐标
        y0 = round(self.screen_size[1] * 0.12 * num - bt.get_height() / 2)
        # 计算按钮y结束坐标
        y1 = y0 + bt.get_height()
        return [[x0, y0], [x1, y1]]

    def click(self, button_images, cursor_x, cursor_y, is_click):
        """
        菜单选择
            choice：菜单选择内容标记，1为初临乱世，2为乱世再起，3为退隐山林
            cursor：加载鼠标图像
            coo：存放所有菜单按钮坐标范围
        :param button_images: 菜单按钮图像
        :param cursor_x: 鼠标x坐标
        :param cursor_y: 鼠标y坐标
        :param is_click: 鼠标点击事件开关
        :return: choice
        """
        # 初始化惨淡选择标记
        choice = 0
        # 加载鼠标图像
        cursor = game.image.load(self.cursor_image)
        # 初始化按钮坐标范围
        coo = list()
        # 循环每一个按钮图像，进行按钮图像绘制及坐标范围获取
        for i in range(len(button_images)):
            coo.append(self.menu(button_images[i], i + 4))
        # 依据鼠标位置与按钮坐标范围判断鼠标是否与按钮碰撞并点击，如果是，分别对相应按钮坐标点击事件进行标记
        if (coo[0][0][0] <= round(cursor_x - cursor.get_width() / 2) <= coo[0][1][0] and
                coo[0][0][1] <= round(cursor_y - cursor.get_height() / 2) <= coo[0][1][1]):
            self.menu(button_images[0], 0 + 4)
            if is_click:
                choice = 1
        if (coo[1][0][0] <= round(cursor_x - cursor.get_width() / 2) <= coo[1][1][0] and
                coo[1][0][1] <= round(cursor_y - cursor.get_height() / 2) <= coo[1][1][1]):
            self.menu(button_images[1], 1 + 4)
            if is_click:
                choice = 2
        if (coo[2][0][0] <= round(cursor_x - cursor.get_width() / 2) <= coo[2][1][0] and
                coo[2][0][1] <= round(cursor_y - cursor.get_height() / 2) <= coo[2][1][1]):
            self.menu(button_images[2], 2 + 4)
            if is_click:
                choice = 3
        # 绘制鼠标图像
        self.cursor(cursor_x, cursor_y)
        return choice
