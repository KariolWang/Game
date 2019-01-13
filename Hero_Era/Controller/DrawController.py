#! D:/Tools/Python35
from Hero_Era.View import Drawing
from Hero_Era.Controller.GameInit import game, clock


class DrawInterface(object):
    
    def __init__(self):
        self.game = game
        self.clock = clock
        self.size = (1280, 720)
        self.screen_title = 'Python单机游戏-乱世君临'
        self.menu_bg_image = 'Media/images/menuBackground.png'
        self.newGame_bg_image = 'Media/images/newGameBackground.jpg'
        self.menu_bg_music = 'Media/music/menu.mp3'
        self.cursor = 'Media/images/cursorImage.png'
        self.topic = 'Media/images/gameTitleImage.png'
        self.icon = 'Media/images/iconImage.png'
        self.menu_buttons = [
            'Media/images/startGameButton.png',
            'Media/images/continueGameButton.png',
            'Media/images/endGameButton.png'
        ]
        self.newGame_buttons = [
            'Media/images/createHeroImage0.png',
            'Media/images/choiceGroupImage0.png',
            'Media/images/createHeroButton.png',
            'Media/images/choiceGroupButton.png'
        ]
        self.newGame_buttons_hover = [
            'Media/images/createHeroImage.png',
            'Media/images/choiceGroupImage.png',
            'Media/images/createHeroButton.png',
            'Media/images/choiceGroupButton.png'
        ]
        self.is_fill = False
        self.count = -1
    
    def running(self):
        is_over_menu = self.menu_interface()
        if is_over_menu == 1:
            print('初临乱世')
            is_over = self.new_game_interface()
            if is_over in [1, 3]:
                print('英雄出世')
            if is_over in [2, 4]:
                print('选择势力')
        if is_over_menu == 2:
            print('乱世再起')
    
    def menu_interface(self):
        dm = Drawing.DrawMenu(self.size, self.screen_title, self.is_fill, self.icon,
                              self.cursor,  self.count, self.topic)
        dm.play_music(self.menu_bg_music, self.count)
        run = True
        is_over = 0
        while run:
            self.clock.tick(30)
            is_click = False
            x, y = self.game.mouse.get_pos()
            dm.draw_image(self.menu_bg_image, (0, 0))
            dm.draw_topic()
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    exit()
                if event.type == self.game.MOUSEBUTTONDOWN:
                    is_click = True
            coo, excursion = dm.draw_menus(self.menu_buttons)
            is_over = dm.buttons_click(x, y, coo, self.menu_buttons, excursion)
            if is_over == 1 and is_click:  # 初临乱世
                run = False
            if is_over == 2 and is_click:  # 乱世再起
                run = False
            if is_over == 3 and is_click:  # 退隐山林
                exit()
            dm.draw_cursor(x, y)
            self.game.display.flip()
            self.game.display.update()
        return is_over
            
    def new_game_interface(self):
        dm = Drawing.DrawNewGame(self.size, self.screen_title, self.is_fill, self.icon,
                                 self.cursor, self.newGame_bg_image)
        run = True
        is_over = 0
        while run:
            self.clock.tick(30)
            is_click = False
            x, y = self.game.mouse.get_pos()
            dm.draw_image(self.newGame_bg_image, (0, 0))
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    exit()
                if event.type == self.game.MOUSEBUTTONDOWN:
                    is_click = True
            coo, excursion = dm.draw_menus(self.newGame_buttons)
            is_over = dm.buttons_click(x, y, coo, self.newGame_buttons_hover, excursion)
            if is_over in [1, 3] and is_click:  # 英雄出世
                run = False
            if is_over in [2, 4] and is_click:  # 选择势力
                run = False
            dm.draw_cursor(x, y)
            self.game.display.flip()
            self.game.display.update()
        return is_over
