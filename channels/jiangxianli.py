# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  JiangXianLI.py
@Time    :  2022/4/16 18:33
@Author  :  Mz100
@Desc    :  None
"""

from libs.spider_requests import Spider


class JiangXianLi(Spider):

    def __init__(self):
        self.base_url = "https://ip.jiangxianli.com/"
        self.source = 3
