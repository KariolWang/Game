#! D:/Tools/Python35
from Hero_Era.Model import Hero
from Hero_Era.Controller.DrawController import DrawInterface

if __name__ == '__main__':
    hero = Hero.Hero('岳飞', 4)
    DrawInterface().running(hero)
