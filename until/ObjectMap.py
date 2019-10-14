# encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

"""
本文件用于实现定位页面元素的公共方法
"""


# 获取单个页面元素
def getElement(driver, locateType, locatorExpresion):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locateType, value=locatorExpresion))
        return element
    except Exception as e:
        raise e


# 获取多个相同元素对象，以list返回
def getElements(driver, locateType, locatorExpresion):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType, value=locatorExpresion))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver

    # 进行单元测试
    driver = webdriver.Chrome(executable_path="D:\\chromedriver")
    driver.get("https://www.baidu.com/")
    searchBox = getElement(driver, "id", "kw")
    # 打印标签名
    print(searchBox.tag_name)
    aList = getElements(driver, "tag name", "a")
    print(len(aList))
    driver.quit()
