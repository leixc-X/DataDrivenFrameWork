# encoding=utf-8
from until.ObjectMap import *
from until.ParseConfigurationFile import ParseCofigFile

"""
此文件用于编写126邮箱登录页面的页面元素对象
"""


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.loginOptions = self.parseCF.getItemsSection("126mail_login")
        print(self.loginOptions)

    def switchInput(self):
        try:
            # 从定位表达式配置文件读取定位输入框按钮的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.input".lower()].split(">")
            # 获取登录页面的输入登录方式按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def switchToFrame(self):
        # 通过正则表达式配置文件中读取frame的定位表达式
        locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
        self.driver.switch_to.frame(driver.find_element_by_tag_name(locatorExpression))

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNmaeObj(self):
        try:
            # 从定位表达式配置文件读取定位用户名输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            # 获取登录页面的用户名输入框对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            # 从定位表达式配置文件读取定位密码输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            # 从定位表达式配置文件读取定位登录按钮的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            # 获取登录页面的登录按钮框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e


if __name__ == '__main__':
    # 测试代码
    from selenium import webdriver
    import time

    driver = webdriver.Chrome(executable_path="D:\\chromedriver")
    driver.get("https://mail.126.com/")
    time.sleep(5)
    login = LoginPage(driver)
    login.switchInput().click()
    # driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div/iframe"))
    login.switchToFrame()
    # 输入用户名密码
    login.userNmaeObj().send_keys("leixiaochen97")
    login.passwordObj().send_keys("qwe892156972***")
    login.loginButton().click()
    time.sleep(5)
    login.switchToDefaultFrame()
    driver.quit()
