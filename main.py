# !/venv/Scripts/python.exe
# -*- coding: utf-8 -*-
"""
@File    :  main.py
@Time    :  2022/4/16 16:58
@Author  :  Mz100
@Desc    :  IP代理池建池主程序
"""

import os
from libs.sqlite import Sqlite
from channels.kuaidaili import Kuaidaili
from channels.ipfree import IpFree
from channels.jiangxianli import JiangXianLi
import threading

def run():

    try:
        print('''请选择获取的ip提供商：
    1. 快代理
    2. 89免费代理 
    3. 高可用全球免费代理ip库
    4. 全部''')
        channel = input('请输入选项(数字)：')
        if channel == '1':
            Kuaidaili().run()
        elif channel == '2':
            IpFree().run()
        elif channel == '3':
            JiangXianLi().run()
        elif channel == '4':
            # 多线程处理
            channels = [
                Kuaidaili().run,
                IpFree().run,
                JiangXianLi().run
            ]
            # 创建线程
            threads = []
            for i in channels:
                threads.append(threading.Thread(target=i))
            # 启动线程
            for i in threads:
                i.start()
            # 等待线程结束
            for i in threads:
                i.join()

        else:
            raise Exception('输入错误！')
    except Exception as e:
        print('输入错误，请重新输入！')
        run()

if __name__ == '__main__':
    db = Sqlite()
    if db.get_db_file():
        run()
