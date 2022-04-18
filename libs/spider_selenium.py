# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  spider_selenium.py
@Time    :  2022/4/17 11:53
@Author  :  Mz100
@Desc    :  爬虫主程序，使用 selenium
"""

from selenium import webdriver
from libs.spider_base import SpiderBase


class Spider(SpiderBase):

    # 爬取数据
    def spider(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url=self.base_url)
        # 编码处理
        data = browser.page_source
        browser.quit()
        return data
