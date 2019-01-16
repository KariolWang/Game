#! D:/Tools/Python35
from Hero_Era.Model.DBConn import Conn
from Hero_Era.Controller.ConnController import ConnController
from Hero_Era.Controller.DrawController import DrawInterface


class Run(object):
    
    def __init__(self, db_name, hero_table, name):
        self.Conn = Conn(db_name)   # DBConn模块
        self.conn = self.Conn.conn  # 数据库连接对象
        self.cursor = self.conn.cursor()    # 操作指针
        self.hero_table = hero_table    # 英雄表名
        self.name = name    # 英雄名

    def running(self):
        """
        运行逻辑控制
        :return: None
        """
        is_over_menu = DrawInterface().menu_interface()
        if is_over_menu == 1:
            print('初临乱世')
            is_over = DrawInterface().new_game_interface()
            if is_over in [1, 3]:
                self.Conn.create_heroes_table()
                print('英雄出世')
                heroes = ConnController(self.name).hero()
                is_over_hero = DrawInterface().new_hero_interface(heroes[1])
                while True:
                    if is_over_hero == 1:
                        print('成功创建英雄{}'.format(heroes[1][1][0]))
                        self.Conn.inert_data(self.hero_table, heroes[0])
                        break
                    if is_over_hero == 2:
                        heroes = ConnController(self.name).hero()
                        is_over_hero = DrawInterface().new_hero_interface(heroes[1])
            if is_over in [2, 4]:
                print('选择势力')
        if is_over_menu == 2:
            print('乱世再起')
