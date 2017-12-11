# -*-coding:utf-8 -*-
from selenium.webdriver.common.by import By
from appium import webdriver
import basepage

'''
淘宝首页涉及元素封装
'''
#driver = webdriver.Remote('http://localhost:4723/wd/hub', basepage.action.capabilities)

class home(basepage.action):

    # 淘宝搜索loc
    search_loc = (By.ID, "com.taobao.taobao:id/home_searchedit")

    # 淘宝搜索框loc
    search_input_loc = (By.ID, "com.taobao.taobao:id/searchEdit")

    # 点击搜索
    def click_search(self):
#        self.find_element(*self.search_loc).click()
         self.click('id', "com.taobao.taobao:id/home_searchedit")

    # 输入搜索关键字
    def input_search(self, words):
 #       self.send_keys(self.search_loc, words)
        self.input('id', "com.taobao.taobao:id/searchEdit", words)

