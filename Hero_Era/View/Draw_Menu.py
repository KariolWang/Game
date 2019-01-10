#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game


class DrawIndex(object):
    def __init__(self, size, screen_title, image, music, cursor, title_image, is_fill):
        self.screen_size = size
        self.screen_title = screen_title
        self.background_image = image
        self.background_music = music
        self.cursor_image = cursor
        self.title_image = title_image
        self.screen = game.display.set_mode(self.screen_size, game.FULLSCREEN if is_fill else 0, 32)

    def music(self):
        game.mixer_music.load(self.background_music)
        game.mixer_music.play(-1)

    def background(self):
        game.display.set_caption(self.screen_title)
        bg = game.image.load(self.background_image)
        self.screen.blit(bg, (0, 0))

    def title(self):
        title = game.image.load(self.title_image)
        x = self.screen_size[0] / 2 - title.get_width() / 2
        y = self.screen_size[1] * 0.15 - title.get_height() / 2
        self.screen.blit(title, (x, y))

    def cursor(self, x, y):
        cursor = game.image.load(self.cursor_image)
        game.mouse.set_visible(False)
        x -= cursor.get_width() / 2
        y -= cursor.get_height() / 2
        self.screen.blit(cursor, (x, y))

    def menu(self, button, num):
        bt = game.image.load(button)
        x = self.screen_size[0] / 2 - bt.get_width() / 2
        y = self.screen_size[1] * 0.12 * num - bt.get_height() / 2
        self.screen.blit(bt, (x, y))
        x0 = round(self.screen_size[0] / 2 - bt.get_width() / 2)
        x1 = x0 + bt.get_width()
        y0 = round(self.screen_size[1] * 0.12 * num - bt.get_height() / 2)
        y1 = y0 + bt.get_height()
        return [[x0, y0], [x1, y1]]

    def click(self, button_images, cursor_x, cursor_y, is_click):
        choice = 0
        cursor = game.image.load(self.cursor_image)
        coo = list()
        for i in range(3):
            coo.append(self.menu(button_images[i], i + 4))
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
        self.cursor(cursor_x, cursor_y)
        return choice
