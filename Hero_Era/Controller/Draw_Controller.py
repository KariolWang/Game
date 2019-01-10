#! D:/Tools/Python35
from Hero_Era.View.Draw_Mode import DrawMode


class DrawIndex(object):
    
    def __init__(self):
        self.size = (1280, 720)
        self.title = 'Python单机游戏-乱世君临'
        self.b_image = 'Media/images/bg.png'
        self.b_music = 'Media/music/menu.mp3'
        self.is_fill = False
        self.count = -1
        self.topic = 'Media/images/title.png'
        self.buttons = [
            'Media/images/start.png',
            'Media/images/continue.png',
            'Media/images/end.png'
        ]
    
    def draw_index(self):
        DrawMode(
            self.size, self.title, self.is_fill, self.b_image, self.b_music, self.count, self.topic, self.buttons
        ).menu()
