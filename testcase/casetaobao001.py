# -*- coding:utf-8 -*-

from po import homepage, basepage
from appium import webdriver
import unittest
import time
class TestTaobao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', basepage.action.capabilities)
        self.homepage = homepage.home(self.driver)
    def test_Search(self):
        '''测试淘宝搜索'''
        self.homepage.click_search()
        self.homepage.input_search('yoyoketang')

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
