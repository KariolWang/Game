#! D:/Tools/Python35
import configparser
from Hero_Era.Controller.Controller import Run

if __name__ == '__main__':
    """
    运行游戏
    """
    # 加载配置文件
    cp = configparser.ConfigParser()
    cp.read('conf.cfg', encoding='utf-8')
    # 数据库文件名称
    db_name = cp.get('DB', 'dbf_name')
    # 英雄表名
    h_table = cp.get('DB', 'htb_name')
    # 势力表名
    g_table = cp.get('DB', 'gtb_name')
    # 英雄装备表名
    he_table = cp.get('DB', 'het_name')
    # 装备表名
    e_table = cp.get('DB', 'etb_name')
    # 英雄名
    name = cp.get('HERO', 'name')
    # 启动游戏
    Run(db_name, h_table, name).running()
