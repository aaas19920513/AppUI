# -*-coding:utf-8-*-
from selenium.common.exceptions import WebDriverException
import readConfig
import AdbPhone
import threading
from appium import webdriver
cf = readConfig.ReadConfig()


class MyDriver:

    driver = None
    # 创建进程锁
    mutex = threading.Lock()
    phoneInit =AdbPhone.Init()
    platformName = cf.getConfigValue("platformName")
    platformVersion = phoneInit.get_android_version()
    appPackage = cf.getConfigValue("appPackage")
    appActivity = cf.getConfigValue("appActivity")
    deviceName = phoneInit.get_deviceName()
    baseUrl = cf.getConfigValue("baseUrl")
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage,
                    "appActivity": appActivity, "deviceName": deviceName}

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


MyDriver.get_driver()