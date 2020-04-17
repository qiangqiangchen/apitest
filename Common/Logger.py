# -*- coding: UTF-8 -*-
import logging
import os
import time


class Logger:
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler,用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%', time.localtime(time.time()))
        log_path = ''  # log保存路径
        log_name = os.path.join(log_path, rq + '.log')
        # 创建一个handler，保存到日志文件
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 创建一个handler，输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
