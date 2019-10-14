# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appModules.LoginAction import LoginAction
from until.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.AddContactPersonAction import AddContactPerson
import traceback
from time import sleep
from until.Log import *

# 设置此次测试环境的环境编码为UTF-8
import importlib, sys

importlib.reload(sys)

# 创建解析Excel对象
exceObj = ParseExcel()
# 将Excel数据文件加载到内存
exceObj.loadWorkBook(dataFilePath)


def LaunchBrowser():
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options对象添加禁用扩展插件设置参数
    chrome_options.add_argument("--disable-extensions")
    # 添加屏蔽提示信息ignore-certificate-errors的设置参数
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # 窗口初始最大化
    chrome_options.add_argument('--start-maximized')
    # 启动带有自定义设置的谷歌浏览器
    driver = webdriver.Chrome(executable_path="d:\\chromedriver", chrome_options=chrome_options)
    # 登录126网址
    driver.get("https://mail.126.com/")
    sleep(3)
    return driver


def test126MailAddContacts():
    logging.info(u"126邮箱添加联系人数据驱动测试开始...")
    try:
        # 根据Excel文件中sheet名称获取sheet对象
        userSheet = exceObj.getSheetByName(u"126帐号")
        # 获取126帐号的sheet中的是否执行
        isExecuteUser = exceObj.getColumn(userSheet, account_isExecute)
        # 获取126帐号的sheet中的数据列表
        dataBookColumn = exceObj.getColumn(userSheet, account_dataBook)

        # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for idx, i in enumerate(isExecuteUser[1:]):
            # 循环遍历126帐号表中的帐号，为需要执行账号添加联系人
            if i.value == "y":      # y表示需要执行
                # 获取第i行的数据
                userRow = exceObj.getRow(userSheet, idx + 2)
                # 获取第i行的用户名
                username = userRow[account_username - 1].value
                # 获取第i行的密码
                password = str(userRow[account_password - 1].value)
                # 打印用户名 密码
                print(username, password)

                # 创建浏览器实例对象
                driver = LaunchBrowser()
                logging.info(u"启动浏览器，访问126邮箱主页")

                # 登录126邮箱
                LoginAction.login(driver, username, password)
                # 设置等待时长，让浏览器启动完成以便后续操作
                sleep(3)
                try:
                    assert u"收信" in driver.page_source
                    logging.info(u"用户%s登录后，断言页面关键字“收信”成功"% username)
                except AssertionError as e:
                    logging.debug(u"用户%s登录后，断言页面关键字“收信”失败," u"异常信息%s:" % (username,str(traceback.print_exc())))
                # 获取第i行中用户名添加的联系人数据表sheet名
                dataBookName = dataBookColumn[idx + 1].value
                # 获取对象数据表对象
                dataSheet = exceObj.getSheetByName(dataBookName)
                # 获取联系人数据表中的是否执行列的对象
                isExecuteData = exceObj.getColumn(dataSheet, contacts_isExecute)
                contactNum = 0  # 记录添加成功联系人个数
                isExecuteNum = 0  # 记录需要执行联系人个数
                for id, data in enumerate(isExecuteData[1:]):
                    # 遍历循环是否执行添加联系人添加操作
                    # 如果设置被添加，则进行联系人添加操作
                    if data.value == "y":
                        # 如果第id行的联系人被设置为执行 isExecuteNUm 自增1
                        isExecuteNum += 1
                        # 获取联系人第id+2行对象
                        rowContent = exceObj.getRow(dataSheet, id + 2)
                        # 获取联系人姓名
                        contactPersonName = rowContent[contacts_contactPersonName - 1].value
                        # 获取联系人邮箱号
                        contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
                        # 获取联系人是否为星标联系人
                        isStar = rowContent[contacts_isStar - 1].value
                        # 获取联系人手机号
                        contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
                        # 获取联系人备注信息
                        contactPersonComment = rowContent[contacts_contactPersonComment - 1].value
                        # 添加成果后，断言关键字
                        assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
                        print(contactPersonName, contactPersonEmail, assertKeyWord)
                        print(contactPersonPhone, contactPersonComment, isStar)
                        # 执行新建联系人操作
                        AddContactPerson.add(driver, contactPersonName, contactPersonEmail, isStar, contactPersonPhone,
                                             contactPersonComment)
                        sleep(1)
                        logging.info(u"添加联系人%s成功" % contactPersonEmail)

                        # 在联系人工作表中写入添加联系人执行时间
                        exceObj.writCellCurrentTime(dataSheet, rowNo=id + 2, colsNo=contacts_runTime)
                        try:
                            # 断言关键是否在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            # 断言失败就在联系人工作表中添加联系人测试失败信息
                            exceObj.writeCell(dataSheet, "faild", rowNo=id + 2, colsNo=contacts_testResult, style="red")
                            logging.info(u"断言关键字%s 失败" % assertKeyWord)
                        else:
                            # 反之为成功
                            exceObj.writeCell(dataSheet, "pass", rowNo=id + 2, colsNo=contacts_testResult,
                                              style="green")
                            # 成功的时候 成功添加联系人数量自增1
                            contactNum += 1
                            logging.info(u"断言关键字%s 成功" % assertKeyWord)
            else:
                logging.info(u"联系人%s被忽略执行" % contactPersonEmail)
            # print("contactNum = %s, isExecuteNum = %s" % (contactNum, isExecuteNum))
            if contactNum == isExecuteNum:
                # 如果成功添加联系人数与需要添加联系人数相等
                # 说明给第i个用户添加联系人测试用例执行成功
                # 在126帐号工作表中写入成功信息，否则为失败
                exceObj.writeCell(userSheet, "pass", rowNo=idx + 2, colsNo=account_testResult, style="green")
                # print(u"为用户%s添加%d个联系人，测试通过！" % (username, contactNum))
            else:
                exceObj.writeCell(userSheet, "faild", rowNo=idx + 2, colsNo=account_testResult, style="red")
            logging.info(u"为用户%s添加%d个联系人,%d个成功" % (username,isExecuteNum, contactNum))
        else:
            ignoreUserName = exceObj.getCellOfValue(userSheet, rowNo=idx + 2, colsNo=account_username)
            logging.info(u"用户%s被忽略执行"% ignoreUserName)
        driver.quit()
    except Exception as e:
        logging.debug(u"数据驱动框架主程序发生异常，异常信息为：%s" % str(traceback.print_exc()))


if __name__ == '__main__':
    test126MailAddContacts()
    print(u"126邮箱登录成功")
