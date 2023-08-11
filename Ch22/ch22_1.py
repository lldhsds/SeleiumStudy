from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
print(type(browser))
url = 'https://www.baidu.com'
browser.get(url)

# 抓取百度首页不同的html元素
tag1 = browser.find_element(By.TAG_NAME, 'title')
print("标签名称 = %s, 内容是 = %s " % (tag1.tag_name, tag1.text))

tag2 = browser.find_element(By.ID, 'ai-talk-container')
print("\n标签名称 = %s, 内容是 = %s " % (tag2.tag_name, tag2.text))
