# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  spider_requests.py
@Time    :  2022/4/17 11:53
@Author  :  Mz100
@Desc    :  爬虫主程序，使用 requests
"""
import requests
from libs.proxy import Proxy
from libs.spider_base import SpiderBase


class Spider(SpiderBase):

    # 爬取数据
    def spider(self):
        req = requests.get(url=self.base_url, headers=Proxy().get_header(), timeout=5)
        # 编码处理
        req.encoding = req.apparent_encoding

        return req.text
