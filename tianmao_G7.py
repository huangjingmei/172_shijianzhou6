# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:52:34 2019

@author: Administrator
"""

from selenium import webdriver
import time
class TM(object):
    def __init__(self):
        # self.keyword = keyword
        pass
    def start_tm(self):
        driver = webdriver.Firefox()
        driver.get('https://www.tmall.com')
        search_input = driver.find_element_by_id('mq')
        search_input.send_keys('戴尔 G7 7590-1865')
        search_btn = driver.find_element_by_css_selector('button[type="submit"]')
        search_btn.click()
        time.sleep(4)
        file_handle = open('tianmao.txt', 'w', encoding='utf-8')
        for x in range(1,2):
            print('正在获取数据，请稍后。。。。')
            for x in range(1,11,2):
                time.sleep(1)
                j = x/10
                js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
                driver.execute_script(js)
            foods = driver.find_elements_by_class_name('product')
            for food in foods:
                file_handle.write(food.text)
                file_handle.write('\n\n')
        file_handle.close()
        # 退出浏览器
        driver.quit()
print(__name__)
if __name__ == '__main__':
 
    tm = TM()
    tm.start_tm()
