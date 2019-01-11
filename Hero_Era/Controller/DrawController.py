#! D:/Tools/Python35
from Hero_Era.View.Drawing import DrawMenu


class DrawIndex(object):
    
    def __init__(self):
        self.size = (1280, 720)
        self.title = 'Python单机游戏-乱世君临'
        self.b_image = 'Media/images/bg.png'
        self.b_music = 'Media/music/menu.mp3'
        self.cursor = 'Media/images/cursor.png'
        self.topic = 'Media/images/title.png'
        self.icon = 'Media/images/icon.png'
        self.buttons = [
            'Media/images/start.png',
            'Media/images/continue.png',
            'Media/images/end.png'
        ]
        self.is_fill = False
        self.count = -1
    
    def draw_index(self):
        DrawMenu(
            self.size, self.title, self.is_fill, self.b_image, self.b_music,
            self.count, self.topic, self.buttons, self.icon, self.cursor
        ).menu()
