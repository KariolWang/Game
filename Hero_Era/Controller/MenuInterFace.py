#! D:/Tools/Python35
from Hero_Era.View import Draw_Menu as dM


class MenuFace(object):

    def __init__(self, is_fill):
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
        menu = dM.DrawIndex(self.screen_size, self.screen_title, self.background_image, self.background_music,
                            self.cursor_image, self.title_image, self.is_fill)
        menu.background()
        menu.title()
        return menu

    def play_music(self):
        self.background().music()

    def menu_click(self, x, y, is_click):
        return self.background().click(self.button_images, x, y, is_click)
