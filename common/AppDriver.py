# -*-coding:utf-8-*-
__author__ = 'tuihou'

from selenium.common.exceptions import WebDriverException
import readConfig
import AdbPhone
import threading
import AppInfo
from config import globalparameter as gl
from appium import webdriver
cf = readConfig.ReadConfig()


class MyDriver:
    app = AppInfo.ApkInfo(gl.project_path+'\\test.apk')
    driver = None
    # 创建进程锁
    mutex = threading.Lock()
    phoneInit =AdbPhone.Init()
    platformName = cf.getConfigValue("platformName")
    platformVersion = phoneInit.get_android_version()
    appPackage = app.getApkPackagename()
    appActivity = app.getApkActivity()
#    print type(appActivity)
#    print appPackage, appActivity
    appPackage1 = cf.getConfigValue("appPackage")
    appActivity1 = cf.getConfigValue("appActivity")
#    print type(appActivity1)
    deviceName = phoneInit.get_deviceName()
    baseUrl = cf.getConfigValue("baseUrl")
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage1,
                    "appActivity": appActivity1, "deviceName": deviceName}

    def _init__(self):
        pass

    @staticmethod
    def get_driver():

        try:
            if MyDriver.driver is None:
                MyDriver.mutex.acquire()
                if MyDriver.driver is None:

                    try:

                        MyDriver.driver = webdriver.Remote(MyDriver.baseUrl, MyDriver.desired_caps)
                    except :
                        MyDriver.driver = None

                MyDriver.mutex.release()

            return MyDriver.driver
        except WebDriverException:
            raise

if __name__ =='__main__':
    MyDriver.get_driver()