# -*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
from appium import webdriver
import basepage

'''
美团首页涉及元素封装
'''
driver = webdriver.Remote('http://localhost:4723/wd/hub', basepage.action.capabilities)

class home(basepage.action):

    # 美团首页搜索loc
    search_loc = (By.ID, "com.sankuai.meituan.takeoutnew:id/bc_")

    # 美团搜索输入框loc
    searchInput_loc = (By.ID, "com.sankuai.meituan.takeoutnew:id/age")

    # 搜索Button
    search_button_loc = (By.ID, "com.sankuai.meituan.takeoutnew:id/agc")

    # 点击搜索
    def click_search(self):
        self.find_element(*self.search_loc).click()

    # 输入搜索关键字
    def input_search(self, words):
        self.send_keys(self.searchInput_loc, words)

    def click_search_button(self):
        self.find_element(*self.search_button_loc)