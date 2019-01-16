#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game


class Drawing(object):

    def __init__(self, size, title, is_fill, icon, cursor):
        self.game = game    # pygame初识化对象
        self.s_size = size     # 游戏窗口大小
        self.s_title = title    # 游戏窗口标题
        self.is_fill = is_fill  # 是否全屏
        self.icon = icon       # 游戏窗口图标
        self.cursor = cursor    # 鼠标图像
        self.cursor_load = game.image.load(self.cursor)     # 加载鼠标图像
        self.game.display.set_caption(self.s_title)     # 设置游戏窗口标题
        self.game.display.set_icon(self.game.image.load(self.icon))     # 设置游戏窗口图标
        self.screen = self.game.display.set_mode(
            self.s_size, self.game.FULLSCREEN if self.is_fill else self.game.DOUBLEBUF, 32)     # 绘制窗口
    
    def draw_image(self, image, coord):
        """
        绘制图像
        :param image: 图像文件名
        :param coord: 图像坐标
        :return: None
        """
        self.screen.blit(self.game.image.load(image), coord)
        
    def draw_font(self, font, size, text, color, coord):
        """
        绘制文字
        :param font: 字体文件名
        :param size: 字号
        :param text: 文字内容
        :param color: 文字颜色
        :param coord: 文字坐标
        :return: None
        """
        font = self.game.font.Font(font, size)
        msg = font.render(text, True, color)
        self.screen.blit(msg, coord)
    
    def play_music(self, music, count):
        """
        播放音乐
        :param music: 音乐文件名
        :param count: 循环次数
        :return: None
        """
        self.game.mixer_music.load(music)
        self.game.mixer_music.play(count)
    
    def draw_cursor(self, x, y):
        """
        绘制鼠标
        :param x: 鼠标x坐标
        :param y: 鼠标y坐标
        :return: None
        """
        self.game.mouse.set_visible(False)
        x -= self.cursor_load.get_width()/4
        y -= self.cursor_load.get_height()/4
        self.draw_image(self.cursor, (x, y))
    
    def buttons_click(self, x, y, coo, buttons, excursion):
        """
        按钮点击
        :param x: 鼠标x坐标
        :param y: 鼠标y坐标
        :param coo: 图像坐标范围
        :param buttons: 图像文件名列表
        :param excursion: 坐标偏移量
        :return: is_over 按钮编号
        """
        is_over = 0
        for i in range(len(coo)):
            if (coo[i][0][0] <= round(x-self.cursor_load.get_width()/2) <= coo[i][1][0] and
                    coo[i][0][1] <= round(y-self.cursor_load.get_height()/2) <= coo[i][1][1]):
                is_over = i+1
        if is_over != 0:
            bt = self.game.image.load(buttons[is_over-1])
            bx = self.screen.get_width()*excursion[is_over-1][0]-bt.get_width()/2
            by = self.screen.get_height()*excursion[is_over-1][1]-bt.get_height()/2
            self.screen.blit(bt, (bx, by))
        return is_over
    
    @staticmethod
    def excursion(ratio_x, param_x, ratio_y, param_y):
        """
        计算偏移量
        :param ratio_x: x坐标偏移窗口比例
        :param param_x: x坐标偏移参数
        :param ratio_y: y坐标偏移窗口比例
        :param param_y: y坐标偏移参数
        :return: excursion_x x坐标偏移量 excursion_y y坐标偏移量
        """
        excursion_x = ratio_x*param_x
        excursion_y = ratio_y*param_y
        return excursion_x, excursion_y


class DrawMenu(Drawing):

    def __init__(self, s_size, title, is_fill, icon, cursor, topic):
        super(DrawMenu, self).__init__(s_size, title, is_fill, icon, cursor)
        self.topic = topic  # 游戏标题

    def draw_topic(self):
        """
        绘制游戏标题
        :return: None
        """
        topic = self.game.image.load(self.topic)
        x = self.screen.get_width()/2-topic.get_width()/2
        y = self.screen.get_height()*0.15-topic.get_height()/2
        self.draw_image(self.topic, (x, y))

    def draw_menus(self, menus):
        """
        绘制菜单按钮
        :param menus: 菜单按钮文件名列表
        :return: coo 图像坐标范围 excursion 坐标偏移量
        """
        coo = list()
        excursion = list()
        for i in range(len(menus)):
            excursion_x, excursion_y = self.excursion(0.5, 1, 0.12, i+4)
            bt = self.game.image.load(menus[i])
            bx0 = self.screen.get_width()*excursion_x-bt.get_width()/2
            by0 = self.screen.get_height()*excursion_y-bt.get_height()/2
            self.draw_image(menus[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
            excursion.append([excursion_x, excursion_y])
        return coo, excursion


class DrawNewGame(Drawing):

    def __init__(self, s_size, title, is_fill, icon, cursor, new_image):
        super(DrawNewGame, self).__init__(s_size, title, is_fill, icon, cursor)
        self.new_image = new_image  # 新游戏背景图文件名
        
    def draw_menus(self, menus):
        """
        绘制菜单按钮
        :param menus: 菜单文件名列表
        :return: coo 图像坐标范围 excursion 坐标偏移量
        """
        coo = list()
        excursion = list()
        for i in range(int(len(menus)/2)):
            excursion_x, excursion_y = self.excursion(1, 0.1+(i+1)*0.265, 0.35, 1.2)
            bt = self.game.image.load(menus[i])
            bx0 = self.screen.get_width()*excursion_x-bt.get_width()/2
            by0 = self.screen.get_height()*excursion_y-bt.get_height()/2
            self.draw_image(menus[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
            excursion.append([excursion_x, excursion_y])
        for i in range(int(len(menus)/2), len(menus)):
            excursion_x, excursion_y = self.excursion(1, 0.1+(i-2+1)*0.265, 0.35, 2)
            bt = self.game.image.load(menus[i])
            bx0 = self.screen.get_width()*excursion_x-bt.get_width()/2
            by0 = self.screen.get_height()*excursion_y-bt.get_height()/2
            self.draw_image(menus[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
            excursion.append([excursion_x, excursion_y])
        return coo, excursion
    
    def draw_hero(self, hero, show_image, font, size, color, check_buttons):
        """
        绘制英雄属性界面
        :param hero: 英雄属性列表
        :param show_image: 英雄属性背景图文件名
        :param font: 英雄属性文字文件名
        :param size: 英雄属性文字字号
        :param color: 英雄属性文字颜色
        :param check_buttons: 确定按钮列表
        :return: coo 确定按钮坐标范围 excursion 确定按钮坐标偏移量
        """
        show = self.game.image.load(show_image)
        x = self.screen.get_width()/2-show.get_width()/2
        y = self.screen.get_height()/2-show.get_height()/2
        self.draw_image(show_image, (x, y))
        for i in range(len(hero[0])):
            self.draw_font(font, size, str(hero[0][i]), color,
                           (x+show.get_width()*(0.1+int(i/5)*0.5+0.05), y+show.get_height()*0.1*(i % 5)+0.5))
        for i in range(len(hero[1])):
            self.draw_font(font, size, str(hero[1][i]), color,
                           (x+show.get_width()*(0.1+int(i/5)*0.5+0.15), y+show.get_height()*0.1*(i % 5)+0.5))
        coo = list()
        excursion = list()
        for i in range(len(check_buttons)):
            excursion_x, excursion_y = self.excursion(
                (x+show.get_width())/self.screen.get_width(), 0.04+0.4*(i+1),
                (y+show.get_height())/self.screen.get_height(), 0.9)
            bt = self.game.image.load(check_buttons[i])
            bx0 = self.screen.get_width()*excursion_x-bt.get_width()/2
            by0 = self.screen.get_height()*excursion_y-bt.get_height()/2
            self.draw_image(check_buttons[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
            excursion.append([excursion_x, excursion_y])
        return coo, excursion
