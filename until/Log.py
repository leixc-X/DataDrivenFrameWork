import logging
import logging.config
from config.VarConfig import parentDirPath
"""
此文件用于初始化日志对象

"""

# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\config\Logger.conf")
# 选择一个日志格式
logger = logging.getLogger("example02")  # 或example01

def debug(message):
    # 定义debug级别日志打印方法
    logger.debug(message)

def info(message):
    # 定义info级别日志打印方法
    logger.info(message)

def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)



