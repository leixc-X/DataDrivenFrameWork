#encoding=utf-8
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath
"""
解析储存定位页面元素定位表达式文件，以便获取定位表达式
"""

class ParseCofigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section下所有option键值对
        # 并以字典方式返回
        """注意：
        使用self.cf.items(sectionName)此方法获取到
        配置文件中的options内容均转换成小写
        比如loginPage.frame转换成了loginpage.frame
        """
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        # 获取指定sections下指定的option值
        value = self.cf.get(sectionName, optionName)
        return value

if __name__ == '__main__':
    pc = ParseCofigFile()
    print(pc.getItemsSection("126mail_login"))
    print(pc.getOptionValue("126mail_login", "loginPage.frame"))