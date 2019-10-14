### 项目介绍
> 自动化数据驱动测试框架（基于python语言）
> 本框架使用python3.7+selenium-webdriver3.0 通过Excel文件中“测试数据是否执行”内容为“y”或“n”可自定义选择测试数据，运行RunTest文件后可以再Excel表格中看到运行结果和时间，在Log文件中也可以查看日志文件，方便测试人员查看结果。

1 项目目录结构包含模块和库
		-- appMdules
		-----AddContactPersonAction.py
		-----LoginAction.py
		-- config
		-----Logger.conf
		-----PageElementLocator.ini
		-----VarConfig.py
		-- Log
		-----DataDrivenFrameWork.log
		-- pageObjects
		-----AddressBookPage,py
		-----HomePage.py
		-----LoginPage.py
		-- testData
		-----126邮箱联系人.xlsx
		-- testScript
		-----TestMail126AddContacts.py
		-- until
		-----Log,py
		-----ObjectMap.py
		-----ParseConfigurationFile.py
		-----ParseExcel.py
		-- RunTest.py

--------------
2 	各个模块和库的介绍
- appMdules里面的Package封装了常用页面对象的方法，简化了测试脚本编写的工作量
- config包含配置文件以及配置文件的设置
-  pageObjects封装了页面元素，方便代码调用，实现了一处维护全局生效的目标。
-  testData包含所测试所需要的数据Excel文件，需要添加多条数据直接修改Excel文件即可
-  until包含了定位页面元素的公共方法，使用ObjectMap方式，简化页面的定位相关的代码量
-  RunTest.py文件是整个框架运行的主入口文件。

----------
3 安装配置
- git clone到本地之后，下载谷歌浏览器的驱动文件（注意更改路径），如果需要使用火狐浏览器更改TestMail126AddContacts.py中的LaunchBrowser方法即可。
- 输入测试数据添加到testData的Excel文件中
- 运行RunTest.py即可
			
		
	