# 说明
Appium +python 2.7+unittest android 

## 第三方库
- xlrd
- requests

##模块说明
common 封装公共方法
- AdbPhone 封装adb所需操作
- App_keywords 封装关键字
- AppDriver 启动 webdriver
- AppInfo 获取 App 的基本所需信息
- AppiumServer 封装启动服务、关闭服务、检查服务方法
- log 定义 log 方法
- send_mail  发送邮件方法
- step_runner buildstepparse

config 全局配置参数

data 存放测试数据
- 在 cecel 编写用例时，切忌空格！！！
- 见 test.xlsx

log 记录log

po pageobject 文件夹

report 存放测试报告

testcase 存放测试用例

config.ini 配置文件

readConfig 读取配置文件方法

Run_all_case 运行所有测试用例

test.apk 测试 APK

