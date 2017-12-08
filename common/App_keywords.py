# -*-coding:utf-8 -*-
from AppDriver import MyDriver
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
import time, os
import log

class Action():


    def __init__(self):

        global driver
        driver = MyDriver.get_driver()
        self.applog = log.log()


    def find_element(self, *loc):
        """
        重写元素定位方法
        """
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return driver.find_element(*loc)
        except AttributeError:
            self.applog.error(u"%s找不到元素%s"% (self, loc))



    def find_elements(self, loc):
        """
        重新封装一组元素定位方法
        """
        try:
            if len(driver.find_elements(*loc)):
                return driver.find_elements(*loc)
        except:
            self.applog.error(u"%s 页面中未能找到 %s 元素" % (self, loc))




    def send_keys(self, loc, value, clear_first=True, click_first=True):
        """
         重写定义send_keys方法,这里的loc格式为（'id','元素名'）
        """
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.applog.error(u"%s找不到元素%s" % (self, loc))


    def click(self, tag, loc):
        """
        重新封装按钮点击方法
        """
        print u'通过'+tag+u'，点击'+loc
        try:
            self.find_element(tag, loc).click()
        except AttributeError:
            self.applog.error(u"点击出错,找不到元素%s" % loc)

    def swipe(self, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return driver.swipe(st, sy, ex, ey, duration=900)

    def get_window_size(self):
        """
        获取屏幕分辨率
        :return: {u'width': 1080, u'height': 1920}
        """
        a = 0
        while a < 6:
            try:
                width = driver.get_window_size()['width']
                height = driver.get_window_size()['height']
                return width, height
            except Exception as e:
                a += 1
                self.applog.error(e)
                self.applog.error('appium failed to get resolution')

    def swipe_ratio(self, st, sy, ex, ey):
        """

        :param st: 起始点宽
        :param sy: 起始点高
        :param ex: 结束点宽
        :param ey: 结束点高
        :return: 滑动动作
        """
        width, height = self.get_window_size()
        return self.swipe(str(st * width), str(sy * height),
                          str(ex * width), str(ey * height))

    def swipe_left(self):
        """
        左滑屏幕
        """
        try:
            self.swipe_ratio(0.8, 0.5, 0.2, 0.5)
        except AttributeError:
            self.applog.error(u'左滑error')

    def swipe_right(self):
        """
        右滑屏幕
        """
        try:
            self.swipe_ratio(0.2, 0.5, 0.8, 0.5)
        except AttributeError:
            self.applog.error(u'右滑error')

    def swipe_up(self):
        """
        上滑屏幕
        """
        try:
            self.swipe_ratio(0.5, 0.8, 0.5, 0.2)
        except AttributeError:
            self.applog.error(u'上滑error')

    def swipe_down(self):
        """
        下滑屏幕
        """
        try:
            self.swipe_ratio(0.5, 0.2, 0.5, 0.8)
        except AttributeError:
            self.applog.error(u'下滑error')


    def save_screenshot(self, file_path):
        """

        :param file_path:
        :return: 获取android设备截图
        """
        try:
            return driver.save_screenshot(file_path)
        except AttributeError:
            self.applog.error(u'截图error')

    def start_activity(self, package, activity):
        """
        启动activity
        package:包名
        activity:.activity
        """
        return driver.start_activity(package, activity)

    def open_notifications(self):
        """
        打开系统通知栏
        """
        return driver.open_notifications()

    def is_app_installed(self, package):
        """
        检查是否安装
        package:包名
        """
        return driver.is_app_installed(package)

    def install_app(self, path):
        """
        安装应用
        path:安装路径
        """
        return driver.install_app(path)

    def remove_app(self, package):
        """
        删除应用
        package:包名
        """
        return driver.remove_app(package)

    def shake(self, ):
        """
        摇晃设备
        """
        return driver.shake()

    def close_app(self, ):
        """
        关闭当前应用
        """
        return driver.close_app()

    def reset_app(self, ):
        """
        重置当前应用
        """
        return driver.reset()

    def current_activity(self, ):
        """
        当前应用的activity
        """
        return driver.current_activity

    def send_key_event(self, arg):
        """
        操作实体按键
        :return:
        """
        event_list = {'entity_home':3, 'entity_back':4, 'entity_menu':82, 'entity_volume_up':24, 'entity_volume_down':25}
        if arg in event_list:
            driver.keyevent(int(event_list[arg]))


    def action_sign(self, action_name, *args):
        """
        带参数的反射函数
        """
        try:
            act = getattr(self, action_name)
            func = act(*args)
            return func
        except AttributeError:
            print u'请检查函数名或者参数是否有误'


    def action(self, action_name):
        """
        不带参数的反射函数
        """
        act = getattr(self, action_name)
        return act()

    # 读取excel文件的table
    @staticmethod
    def readtable(filepath, sheetno):
        """
        filepath:文件路径
        sheetno：Sheet编号
        """
        data = xlrd.open_workbook(filepath)
        # 通过索引顺序获取Excel表
        table = data.sheets()[sheetno]
        return table

    # 读取xls表格，使用生成器yield进行按行存储
    @staticmethod
    def readxls(filepath, sheetno):
        """
        filepath:文件路径
        sheetno：Sheet编号
        """
        table = Action.readtable(filepath, sheetno)
        for args in range(1, table.nrows):
            # 使用生成器 yield
            yield table.row_values(args)

if __name__ == '__main__':

    pass
