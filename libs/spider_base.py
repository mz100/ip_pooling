# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  spider_base.py
@Time    :  2022/4/17 11:53
@Author  :  Mz100
@Desc    :  爬虫主程序，使用 requests
"""
import requests
import sqlite3
import pandas as pd
from libs.sqlite import Sqlite

class SpiderBase:

    def __init__(self):
        self.base_url = ''
        self.source = 0

    # 爬取数据
    def spider(self):

        return ''

    # 管道清理
    def pipeline(self, html):

        tables = pd.read_html(html)
        table = tables[0]
        sources = []
        for i in table['IP']:
            sources.append(self.source)
        # 创建 DataFrame
        df = pd.DataFrame()
        df['ip'] = table['IP']
        df['port'] = table['端口']
        df['address'] = table['位置']
        df['isp'] = table['运营商']
        df['source'] = sources

        return df

    def check_useful(self, df):

        for i, row in df.iterrows():
            if str(row['port']).isdigit():
                check = self.is_useful(row['ip'], row['port'])
                if check == False:
                    df.drop(index=i, inplace=True)
            else:
                df.drop(index=i, inplace=True)

        return df

    # 数据存储
    def save(self, df):
        conn = sqlite3.connect(Sqlite().get_db_file())
        c = conn.cursor()
        if df.values.all():
            for i in df.values:
                if str(i[1]).isdigit():
                    try:
                        sql = "INSERT INTO {5} (ip,port,address,isp,source) VALUES ('{0}', '{1}', '{2}', '{3}','{4}')" \
                            .format(i[0], i[1], i[2], i[3], i[4], Sqlite().get_table())
                        c.execute(sql)
                        conn.commit()
                        print('脚本：' + sql + '插入成功')
                    except Exception as e:
                        print('脚本：' + sql + '插入失败')
                        print(e)
        conn.close()

    def is_useful(self, ip, port):

        url = 'http://icanhazip.com/'
        proxy = str(ip)+":"+str(port)
        proxies = {
            'http': 'http://' + proxy + '/',
            'https': 'https://' + proxy + '/',
        }
        try:
            req = requests.get(url, proxies=proxies, timeout=10)
            if req.status_code == 200:
                print(proxy, '检查能用')
                return True
            else:
                print(proxy, '检查能用')
                return False
        except Exception as e:
            print(proxy, '检查不能用')
            return False

    # 主程序
    def run(self):
        html = self.spider()
        data = self.pipeline(html)
        data = self.check_useful(data)
        self.save(data)
