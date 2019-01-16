#! D:/Tools/Python35
import random


class Hero(object):
    
    def __init__(self, name):
        self.h_name = name  # 英雄名
        self.h_identity = random.randint(1, 4)  # 身份参数
        self.h_lv = 0   # 英雄等级
        self.h_exp = 0  # 英雄经验
        self.h_grade = 1    # 英雄品阶
        self.h_lead = random.randint(15*(self.h_grade-1), 20*self.h_grade)      # 英雄统率
        self.h_force = random.randint(15*(self.h_grade-1), 20*self.h_grade)     # 英雄武力
        self.h_brain = random.randint(15*(self.h_grade-1), 20*self.h_grade)     # 英雄智力
        self.h_politics = random.randint(15*(self.h_grade-1), 20*self.h_grade)  # 英雄政治
        self.h_charm = random.randint(15*(self.h_grade-1), 20*self.h_grade)     # 英雄魅力
        self.h_hp = round(self.h_force*1.8+1)   # 英雄体力
        self.h_sp = round(self.h_brain*1.2+1)   # 英雄技力
        self.h_status = 1   # 英雄状态
    
    def get_exp(self, exp):
        """
        获得经验
        :param exp: 增加的经验
        :return: None
        """
        self.h_exp += exp
        if 50*self.h_grade*self.h_lv*self.h_lv+50 < self.h_exp:
            self.h_lv += 1
            up_attr = round((self.h_grade+1)*0.3)
            if self.h_identity == 1:
                self.h_lead += up_attr
            if self.h_identity == 2:
                self.h_force += up_attr
                self.h_hp += round(up_attr*1.8)
            if self.h_identity == 3:
                self.h_brain += up_attr
                self.h_sp += round(up_attr*1.2)
            if self.h_identity == 4:
                self.h_politics += up_attr
            self.h_hp += round((self.h_grade+1)*1.8)
            self.h_sp += round((self.h_grade+1)*1.2)
