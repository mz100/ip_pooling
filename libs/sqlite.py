# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  sqlite_base.py
@Time    :  2022/4/16 17:18
@Author  :  Mz100
@Desc    :  使用Sqlite存储ip数据
"""

import os
import sqlite3


class Sqlite(object):

    def __init__(self):
        # 数据文件
        self.db_file = os.path.join(
            os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
            'data',
            'ip_pooling.db')
        self.table = 'ip_pooling'
        self.create_table()

    def create_table(self):
        # 数据文件不存在则新增并创建数据表
        if os.path.isfile(self.db_file) == False:
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            c.execute('''create table {0}(
                id integer primary key autoincrement not null ,
                ip char(20) unique not null ,
                port int not null ,
                address char(50) ,
                isp char(50) ,
                source int ,
                is_useful int default 1 ,
                create_dt datetime default (datetime('now', 'localtime')) ,
                lose_dt datetime
                );
            '''.format(self.table))
            conn.commit()
            conn.close()
        return True

    def get_db_file(self):
        if os.path.isfile(self.db_file):
            return self.db_file
        else:
            return False

    def get_table(self):
        return self.table
