#encoding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time
"""
此文件用于实现添加联系人操作的
"""

class AddContactPerson(object):
    def __init__(self):
        print(u"添加联系人")

    @staticmethod
    def add(driver, contactName, contactEmail, isStar, contactPhone, contactComment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            # 点击通讯录连接
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人实例对象
            apd = AddressBookPage(driver)
            apd.createContactPersonButton().click()
            if contactName:
                # 非必填项
                apd.contactPersonName().send_keys(contactName)
                # 非必填项
                apd.contactPersonEmail().send_keys(contactEmail)
                if isStar == u"是":
                    # 非必填项
                    apd.starContacts().click()
                if contactPhone:
                    # 非必填项
                    apd.contactPersonMobile().send_keys(contactPhone)
                if contactComment:
                    apd.contactPersonComment().send_keys(contactComment)
                apd.saveContacePerson().click()
        except Exception as e:
            print(traceback.print_exc())
            raise e


if __name__ == '__main__':

    from LoginAction import LoginAction
    from selenium import webdriver
    import time

    # 打开浏览器
    driver = webdriver.Chrome(executable_path="D:\\chromedriver")
    # 登录126邮箱网址
    driver.get("https://mail.126.com/")
    time.sleep(5)
    LoginAction.login(driver, "leixiaochen97", "qwe892156972***")
    time.sleep(5)
    AddContactPerson.add(driver, u"李坤3", "772172255@qq.com", u"是", "", "")
    time.sleep(3)
    assert u"李坤" in driver.page_source
    driver.quit()
