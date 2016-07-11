# -*- coding: utf-8 -*-
from selenium import webdriver
#引用标准的 unittest 模块
import unittest


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://localhost:8080')
        #网页的标题和头部都包含 todo
        self.assertIn('To-do', self.browser.title())
        # 生成制定的错误消息提醒测试结束
        self.fail('finished the test!')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')
