# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  kuaidaili.py
@Time    :  2022/4/16 18:24
@Author  :  Mz100
@Desc    :  None
"""
import pandas as pd

from libs.spider_selenium import Spider


class Kuaidaili(Spider):

    def __init__(self):
        self.base_url = "https://www.kuaidaili.com/free/"
        self.source = 2

    def pipeline(self, html):

        tables = pd.read_html(html)
        table = tables[0]
        sources = []
        isps = []
        for i in table['位置']:
            sources.append(self.source)
            isps.append(i.split()[-1])
        # 创建 DataFrame
        df = pd.DataFrame()
        df['ip'] = table['IP']
        df['port'] = table['PORT']
        df['address'] = table['位置']
        df['isp'] = isps
        df['source'] = sources

        return df
