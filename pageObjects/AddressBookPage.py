# encoding=utf-8
from until.ObjectMap import *
from until.ParseConfigurationFile import ParseCofigFile


class AddressBookPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.addContactsOption = self.parseCF.getItemsSection("126mail_addContactsPage")
        print(self.addContactsOption)

    def createContactPersonButton(self):
        # 获取新建联系人的按钮
        try:
            # 从定位表达式配置文件读取定位新建联系人按钮的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.createContactsBtn".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        # 获取新建联系人界面姓名输入框
        try:
            # 从定位表达式配置文件读取定位新建联系人姓名输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.contactPersonName".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        # 获取新建联系人界面电子邮件输入框
        try:
            # 从定位表达式配置文件读取定位新建联系人邮箱输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.contactPersonEmail".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        # 获取新建联系人界面星标联系人选择框
        try:
            # 从定位表达式配置文件读取定位新建联系人星标联系人复选框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.starContacts".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        # 获取新建联系人界面联系人手机号输入框
        try:
            # 从定位表达式配置文件读取定位新建联系人手机号输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.contactPersonMobile".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        # 获取新建联系人界面联系人备注信息输入框
        try:
            # 从定位表达式配置文件读取定位新建联系人备注信息输入框的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.contactPersonComment".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def saveContacePerson(self):
        # 获取新建联系人界面联系人保存联系人按钮
        try:
            # 从定位表达式配置文件读取定位新建联系人保存联系人按钮的定位方式和表达式
            locateType, locatorExpression = self.addContactsOption["addContactsPage.saveContacePerson".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e