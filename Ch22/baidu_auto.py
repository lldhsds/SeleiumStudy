from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait           #显示等待模块
from selenium.webdriver.support import  expected_conditions as EC   #判断元素模块
import time
from selenium.webdriver.common.action_chains import ActionChains    #鼠标操作
from selenium.webdriver.support.select import Select        #下拉框处理
from selenium.webdriver.common.keys import Keys

def test_webauto():     #定义测试类名称，也可以理解为建立一个测试用例
    dr = webdriver.chrome
    url = 'https://www.baidu.com'

# 参考https://blog.csdn.net/CJkiss/article/details/113458444