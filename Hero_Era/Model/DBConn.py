#! D:/Tools/Python35
import sqlite3


class Conn(object):
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
    
    def create_heroes_table(self):
        sql = '''CREATE TABLE heroes(
            h_id INTEGER PRIMARY KEY NOT NULL,
            h_name TEXT NOT NULL,
            h_lv INTEGER NOT NULL,
            h_hp INTEGER NOT NULL,
            h_sp INTEGER NOT NULL,
            h_lead INTEGER NOT NULL,
            h_force INTEGER NOT NULL,
            h_brain INTEGER NOT NULL,
            h_politics INTEGER NOT NULL,
            h_charm INTEGER NOT NULL,
            h_grade INTEGER NOT NULL,
            h_status INTEGER NOT NULL
        )'''
        try:
            self.cursor.execute('DROP TABLE {};'.format('heroes'))
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
        
    def inert_data(self, table, data):
        keys = ''
        values = ''
        for key, value in data.__dict__.items():
            keys += '{},'.format(key)
            values += '{},'.format(value)
        sql = '''INSERT INTO {0}({1}) VALUES ({2})'''.format(table, keys[:-1], values[:-1])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
