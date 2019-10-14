#encoding=utf-8
from pageObjects.LoginPage import LoginPage
"""
实现登录模块的封装方法
"""

class LoginAction(object):
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver, username, password):
        try:
            # 实例化对象
            login = LoginPage(driver)
            # 点击按钮
            login.switchInput().click()
            # 进入frame控件
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            # 传入用户名密码
            login.userNmaeObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            # 避免浏览器兼容性问题 退出frame控件
            login.switchToDefaultFrame()
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    # 启动谷歌浏览器
    driver = webdriver.Chrome(executable_path="D:\\chromedriver")
    driver.get("https://mail.126.com/")
    time.sleep(5)
    LoginAction.login(driver, username="leixiaochen97", password="qwe892156972***")
    time.sleep(5)
    driver.quit()