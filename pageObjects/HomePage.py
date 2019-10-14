# encoding=utf-8
from until.ObjectMap import *
from until.ParseConfigurationFile import ParseCofigFile


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()

    def addressLink(self):
        try:
            # 从定位表达式配置文件读取定位通讯录按钮的定位方式和表达式
            locateType, locatorExpression = self.parseCF.getOptionValue("126mail_homePage",
                                                                        "homePage.addressbook").split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e


