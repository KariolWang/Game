#! D:/Tools/Python35
from Hero_Era.View.Drawing import Drawing


class DrawMode(Drawing):
    
    def __init__(self, s_size, title, is_fill, b_image, b_music, count, topic, buttons):
        super(DrawMode, self).__init__(s_size, title, is_fill)
        self.b_image = b_image
        self.b_music = b_music
        self.count = count
        self.topic = topic
    
    def draw_topic(self):
        topic = self.game.image.load(self.topic)
        x = self.screen.get_width()/2-topic.get_width()/2
        y = self.screen.get_height()*0.15-topic.get_height()/2
        self.screen.blit(topic, (x, y))
    
    def draw_buttons(self):
        pass
    
    def menu(self):
        self.play_music(self.b_music, self.count)
        while True:
            self.draw_image(self.b_image, (0, 0))
            self.draw_topic()
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    exit()
            self.game.display.flip()
            self.game.display.update()
