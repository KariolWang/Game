#! D:/Tools/Python35
import random


class Hero(object):
    
    def __init__(self, name, grade):
        self.h_id = 0
        self.h_name = name
        self.h_identity = random.randint(1, 4)
        self.h_lv = 0
        self.h_exp = 0
        self.h_lead = random.randint(random.randint(15, 19)*grade, 99)
        self.h_force = random.randint(random.randint(15, 19)*grade, 99)
        self.h_brain = random.randint(random.randint(15, 19)*grade, 99)
        self.h_politics = random.randint(random.randint(15, 19)*grade, 99)
        self.h_charm = random.randint(random.randint(15, 19)*grade, 99)
        self.h_hp = round(self.h_force*1.8)
        self.h_sp = round(self.h_brain*1.2)
        self.h_grade = grade
        self.h_status = 1
    
    def get_exp(self, exp):
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
