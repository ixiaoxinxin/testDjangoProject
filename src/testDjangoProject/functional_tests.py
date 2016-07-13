# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#引用标准的 unittest 模块
import unittest


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        #添加隐式等待
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        #网页的标题和头部都包含 todo
        self.assertIn('to-do', self.browser.title())
        header_text=self.browser.find_element_by_tag_name('h1').text()#网页的头部包含to-do,这句话是说明如何找头部的信息
        self.assertIn('to-do', header_text)
        
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to do item')
        
        inputbox.send_keys('buy peapock feathers')
        #页面显示输入的内容,只是缓存
        inputbox.send_keys(Keys.ENTER)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text =='1:buy peapock feathers' for row in rows))
        # 生成制定的错误消息提醒测试结束
        self.fail('finished the test!')
    
if __name__ == '__main__':
    unittest.main()
