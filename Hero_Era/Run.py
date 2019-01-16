#! D:/Tools/Python35
import configparser
from Hero_Era.Controller.Controller import Run

if __name__ == '__main__':
    cp = configparser.ConfigParser()
    cp.read('conf.cfg', encoding='utf-8')
    db_name = cp.get('DB', 'dbf_name')
    h_table = cp.get('DB', 'htb_name')
    g_table = cp.get('DB', 'gtb_name')
    he_table = cp.get('DB', 'het_name')
    e_table = cp.get('DB', 'etb_name')
    name = cp.get('HERO', 'name')
    Run(db_name, h_table, name).running()
