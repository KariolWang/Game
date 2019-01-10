#! D:/Tools/Python35
from Hero_Era.Controller.GameInit import game


class Drawing(object):
    
    def __init__(self, s_size, s_title, is_fill):
        self.game = game
        self.s_size = s_size
        self.s_title = s_title
        self.is_fill = is_fill
        self.game.display.set_caption(self.s_title)
        self.screen = self.game.display.set_mode(self.s_size, self.game.FULLSCREEN if self.is_fill else 0, 32)
    
    def draw_image(self, image, coord):
        self.screen.blit(self.game.image.load(image), coord)
    
    def play_music(self, music, count):
        self.game.mixer_music.load(music)
        self.game.mixer_music.play(count)
