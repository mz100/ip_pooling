# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  proxy.py
@Time    :  2022/4/17 14:29
@Author  :  Mz100
@Desc    :  代理
"""
from faker import Faker
import sqlite3
from libs.sqlite import Sqlite


class Proxy:

    def get_header(self):
        return {
            'User-Agent': Faker(locale='zh_CN').user_agent()
        }

    def get_proxy(self):
        conn = sqlite3.connect(Sqlite().get_db_file())
        c = conn.cursor()
        c.execute('select ip , port from ' + Sqlite().get_table() + ' where is_lose = 0 limit 50 ')
        data = c.fetchall()
        conn.close()
        proxies = []
        for i in data:
            proxy = str(i[0]) + ':' + str(i[1])
            proxies.append({'http': 'http://' + proxy, 'https': 'https://' + proxy})
        return proxies
