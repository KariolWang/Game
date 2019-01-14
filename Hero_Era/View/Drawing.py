#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game


class Drawing(object):

    def __init__(self, size, title, is_fill, icon, cursor):
        self.game = game
        self.s_size = size
        self.s_title = title
        self.is_fill = is_fill
        self.icon = icon
        self.cursor = cursor
        self.cursor_load = game.image.load(self.cursor)
        self.game.display.set_caption(self.s_title)
        self.game.display.set_icon(self.game.image.load(self.icon))
        self.screen = self.game.display.set_mode(
            self.s_size, self.game.FULLSCREEN if self.is_fill else self.game.DOUBLEBUF, 32)
    
    def draw_image(self, image, coord):
        self.screen.blit(self.game.image.load(image), coord)
        
    def draw_font(self, font, size, text, color, coord):
        font = self.game.font.Font(font, size)
        msg = font.render(text, True, color)
        coord[0] -= msg.get_width()/2
        coord[1] -= msg.get_height()/2
        self.screen.blit(msg, coord)
    
    def play_music(self, music, count):
        self.game.mixer_music.load(music)
        self.game.mixer_music.play(count)
    
    def draw_cursor(self, x, y):
        self.game.mouse.set_visible(False)
        x -= self.cursor_load.get_width()/4
        y -= self.cursor_load.get_height()/4
        self.draw_image(self.cursor, (x, y))
    
    def buttons_click(self, x, y, coo, buttons, excursion):
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
        excursion_x = ratio_x*param_x
        excursion_y = ratio_y*param_y
        return excursion_x, excursion_y


class DrawMenu(Drawing):

    def __init__(self, s_size, title, is_fill, icon, cursor, topic):
        super(DrawMenu, self).__init__(s_size, title, is_fill, icon, cursor)
        self.topic = topic

    def draw_topic(self):
        topic = self.game.image.load(self.topic)
        x = self.screen.get_width()/2-topic.get_width()/2
        y = self.screen.get_height()*0.15-topic.get_height()/2
        self.draw_image(self.topic, (x, y))

    def draw_menus(self, menus):
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
        self.new_image = new_image
        
    def draw_menus(self, menus):
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
        show = self.game.image.load(show_image)
        x = self.screen.get_width()/2-show.get_width()/2
        y = self.screen.get_height()/2-show.get_height()/2
        self.draw_image(show, (x, y))
        self.draw_font(font, size, hero.h_name, color, (x+show.get_width()*0.3, y+show.get_height()*0.1))
        self.draw_font(font, size, hero.h_lv, color, (x+show.get_width()*0.3, y+show.get_height()*0.2))
        self.draw_font(font, size, hero.h_exp, color, (x+show.get_width()*0.3, y+show.get_height()*0.3))
        self.draw_font(font, size, hero.h_lead, color, (x+show.get_width()*0.3, y+show.get_height()*0.4))
        self.draw_font(font, size, hero.h_force, color, (x+show.get_width()*0.3, y+show.get_height()*0.5))
        self.draw_font(font, size, hero.h_brain, color, (x+show.get_width()*0.3, y+show.get_height()*0.6))
        self.draw_font(font, size, hero.h_politics, color, (x+show.get_width()*0.3, y+show.get_height()*0.7))
        self.draw_font(font, size, hero.h_charm, color, (x+show.get_width()*0.3, y+show.get_height()*0.8))
        self.draw_font(font, size, hero.h_grade, color, (x+show.get_width()*0.3, y+show.get_height()*0.9))
        self.draw_font(font, size, hero.h_identity, color, (x+show.get_width()*0.3, y+show.get_height()*1))
        coo = list()
        excursion = list()
        for i in range(len(check_buttons)):
            excursion_x, excursion_y = self.excursion(
                (x+show.get_width())/self.screen.get_width(), 0.8, (y+show.get_height())/self.screen.get_height(), 0.1*i)
            bt = self.game.image.load(check_buttons[i])
            bx0 = self.screen.get_width()*excursion_x-bt.get_width()/2
            by0 = self.screen.get_height()*excursion_y-bt.get_height()/2
            self.draw_image(check_buttons[i], (bx0, by0))
            bx1 = bx0+bt.get_width()
            by1 = by0+bt.get_height()
            coo.append([[round(bx0), round(by0)], [round(bx1), round(by1)]])
            excursion.append([excursion_x, excursion_y])
        return coo, excursion
