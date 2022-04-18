# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  ipfree.py
@Time    :  2022/4/16 18:33
@Author  :  Mz100
@Desc    :  None
"""

from libs.spider_requests import Spider


class IpFree(Spider):

    def __init__(self):
        self.base_url = 'https://www.89ip.cn/'
        self.source = 2
