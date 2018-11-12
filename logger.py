#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging

#第一步，创建1个logger
LOG_FILE = 'Log_EIPBandwidth'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#第二步，创建1个文件handler，用于日志写入文件
_fh = logging.FileHandler(LOG_FILE)
_fh.setLevel(logging.INFO)
#如果是输出控制台，则创建控制台handler.
_ch = logging.StreamHandler()
_ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
#第三步，定义handler输出格式。
_formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
_fh.setFormatter(_formatter)
#第四步，将logger添加到handler里
logger.addHandler(_fh)

def set_log_file(localfile=None):
	global LOG_FILE
	if LOG_FILE is not None:
		LOG_FILE = localfile
		fh = loggin.FileHandler(LOG_FILE)
		fh.setLevel(logging.INFO)
		fh.setFormatter(_formatter)
		logger.addHandler(fh)


