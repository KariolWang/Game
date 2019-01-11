#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game, clock


class Drawing(object):
    
    def __init__(self, s_size, s_title, is_fill, icon, cursor):
        self.game = game
        self.clock = clock
        self.s_size = s_size
        self.s_title = s_title
        self.is_fill = is_fill
        self.icon = icon
        self.cursor = cursor
        self.cursor_load = game.image.load(self.cursor)
        self.game.display.set_caption(self.s_title)
        self.game.display.set_icon(self.game.image.load(self.icon))
        self.screen = self.game.display.set_mode(self.s_size, self.game.FULLSCREEN if self.is_fill else 0, 32)
    
    def draw_image(self, image, coord):
        self.screen.blit(self.game.image.load(image), coord)
    
    def play_music(self, music, count):
        self.game.mixer_music.load(music)
        self.game.mixer_music.play(count)
    
    def draw_cursor(self, x, y):
        self.game.mouse.set_visible(False)
        x -= self.cursor_load.get_width()/4
        y -= self.cursor_load.get_height()/4
        self.draw_image(self.cursor, (x, y))
    
    def buttons_click(self, x, y, coo):
        is_over = 0
        for i in range(len(coo)):
            self.draw_cursor(x, y)
            if (coo[i][0][0] <= round(x-self.cursor_load.get_width()/2) <= coo[i][1][0] and
                    coo[i][0][1] <= round(y-self.cursor_load.get_height()/2) <= coo[i][1][1]):
                is_over = i+1
        return is_over


class DrawMenu(Drawing):

    def __init__(self, s_size, title, is_fill, b_image, b_music, count, topic, menus, icon, cursor):
        super(DrawMenu, self).__init__(s_size, title, is_fill, icon, cursor)
        self.b_image = b_image
        self.b_music = b_music
        self.count = count
        self.topic = topic
        self.menus = menus

    def draw_topic(self):
        topic = self.game.image.load(self.topic)
        x = self.screen.get_width() / 2 - topic.get_width() / 2
        y = self.screen.get_height() * 0.15 - topic.get_height() / 2
        self.draw_image(self.topic, (x, y))

    def draw_menus(self):
        coo = list()
        for i in range(len(self.menus)):
            bt = self.game.image.load(self.menus[i])
            bx0 = self.screen.get_width()/2-bt.get_width()/2
            by0 = self.screen.get_height()*0.12*(i+4)-bt.get_height()/2
            self.draw_image(self.menus[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
        return coo

    def click_menu(self, x, y, coo, is_click):
        is_over = self.buttons_click(x, y, coo)
        if is_over != 0:
            bt = self.game.image.load(self.menus[is_over-1])
            bx = self.screen.get_width()/2-bt.get_width()/2
            by = self.screen.get_height()*0.12*(is_over-1+4)-bt.get_height()/2
            self.screen.blit(bt, (bx, by))
        if is_over == 1 and is_click:   # 初临乱世
            print('初临乱世')
        if is_over == 2 and is_click:   # 乱世再起
            print('乱世再起')
        if is_over == 3 and is_click:   # 退隐山林
            print('退隐山林')
            exit()

    def menu(self):
        self.play_music(self.b_music, self.count)
        while True:
            is_click = False
            x, y = self.game.mouse.get_pos()
            clock.tick(30)
            self.draw_image(self.b_image, (0, 0))
            self.draw_topic()
            coo = self.draw_menus()
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    exit()
                if event.type == self.game.MOUSEBUTTONDOWN:
                    is_click = True
                self.click_menu(x, y, coo, is_click)
            self.draw_cursor(x, y)
            self.game.display.flip()
            self.game.display.update()
