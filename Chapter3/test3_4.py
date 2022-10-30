# python模块，以.py结尾的python文件，模块可以用来定义函数、类和变量。以下为三种导入方法。

import math
import os
import time

print(math.sqrt(9))

from math import sqrt
print(sqrt(16))

from math import *
print(sqrt(25))
print(sin(180))

# os模块，用于实现访问操作系统等相关功能。

print("一、操作系统信息获取")
print("1、获取操作系统路径的分隔符。windows-\\,Linux/macOS-/")
print(os.sep)
print("2、显示工作平台。windows-nt,Linux/macOS-posix")
print(os.name)
print("3、获取当前文件的目录")
print(os.getcwd())
print("4、拼接文件")
cur_path = os.getcwd()
print(cur_path)
file = cur_path + os.sep + 'test.py'
print(file)

print("二、目录操作")
print("1、返回目录下面的文件和目录")
print(os.listdir('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\'))
print("2、创建、删除文件和目录")
if os.path.exists('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\testdir'):
    # 如果存在目录testdir，执行删除
    os.rmdir('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\testdir')
else:
    # 不存在目录则创建
    os.mkdir('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\testdir')

print("3、创建、删除多层递归目录")
os.makedirs('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\dir1\\subdir1\\')
# 等待3s后删除创建的目录
time.sleep(3)
os.removedirs('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\dir1\\subdir1\\')

print("4、文件管理操作，重命名、获取文件名、获取文件目录、获取文件大小、获取绝对路径、连接目录与目录或文件")
os.mkdir('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\test\\')
os.chdir('C:\\Users\\xushuai\\PycharmProjects\\SeleniumProject\\Chapter3\\test\\')
f = open("test.txt","w",encoding='utf8')
f.write('测试文件管理。')
f.close
