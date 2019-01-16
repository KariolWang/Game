#! D:/Tools/Python35
from Hero_Era.Model.Hero import Hero


class ConnController(object):
    
    def __init__(self, name):
        self.hero_list = list()     # 英雄属性列表
        self.name = name       # 英雄姓名
    
    def hero(self):
        """
        英雄属性转换为列表存储
        :return: hero 英雄对象 hero_list 英雄属性列表
        """
        hero = Hero(self.name)
        self.hero_list.append(['姓名', '体力', '统率', '智力', '魅力', '身份', '技力', '武力', '政治', '品阶'])
        identity = '统帅' if hero.h_identity == 1 else '武将' if hero.h_identity == 2\
            else '军师' if hero.h_identity == 3 else '宰辅'
        self.hero_list.append([hero.h_name, hero.h_hp, hero.h_lead, hero.h_brain, hero.h_charm, identity,
                               hero.h_sp, hero.h_force, hero.h_politics, hero.h_grade])
        return [hero, self.hero_list]
