# -*- coding:utf-8 -*-

from po import MThomepage,basepage
from appium import webdriver
import unittest

class TestTaobao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', basepage.action.capabilities)
        self.homepage = MThomepage.home(self.driver)

    def test_Search(self):
        u'''测试美团外卖搜索'''
        self.homepage.click_search()
        self.homepage.input_search(u'包子')
        self.homepage.click_search_button()
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()