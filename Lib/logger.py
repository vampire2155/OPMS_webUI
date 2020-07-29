# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/8 15:44

import logging,time,os
from config.globalparam import log_path

class Log():
    def __init__(self):
        self.logfile_name = os.path.join(log_path,f"{time.strftime('%Y-%m-%d-%H-%M-S')}.log")

    def printlog(self,level,message):
        #创建一个logger
        logger = logging.getLogger()
        #设置log的默认级别，下面设置的是DEBUG级别， 如果设置的级别比之后要调用的日志的级别高，则调用的logging语句将不会输出。
        #即如果设置为 logging.INFO，如果调用是日志级别是 DEBUG，则此时不会输出日志。
        ''' 日志级别如下：
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
        '''
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，把日志写入到文件中。
        file_handler = logging.FileHandler(filename=self.logfile_name,mode='a',encoding='utf8',delay=False)
        #  创建一个handler，把日志输出到控制台上
        console_handler = logging.StreamHandler()
        #指定日志的最低输出级别，默认为WARN级别
        file_handler.setLevel(logging.DEBUG)
        console_handler.setLevel(logging.DEBUG)
        #定义日志的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        #给logger（logger的作用：提供日志接口）添加 一个handler（handler的作用：将日志记录（log record）发送到合适的目的地（destination），比如文件，socket等）

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        #记录日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(file_handler)
        logger.removeHandler(console_handler)
        #关闭打开的日志文件
        file_handler.close()
        console_handler.close()

    def debug(self,message):
        self.printlog('debug',message)

    def info(self,message):
        self.printlog('info',message)

    def warning(self,message):
        self.printlog('warning',message)

    def error(self,message):
        self.printlog('error',message)

# 实例化一个对象
LogAction = Log()














