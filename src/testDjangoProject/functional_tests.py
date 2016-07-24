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

    #辅助方法类,设计具体要做什么事情
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    #单元测试要做的操作
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://127.0.0.1:8000')
        #网页的标题和头部都包含 todo
        self.assertIn('To-Do', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text()#网页的头部包含to-do,这句话是说明如何找头部的信息
        self.assertIn('To-Do', header_text)
        
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to do item')
        
        inputbox.send_keys('buy peapock feathers')
        #页面显示输入的内容,只是缓存
        inputbox.send_keys(Keys.ENTER)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        #待办事项表格中显示'1:buy peapock feathers' 
        self.assertTrue(
            any(row.text =='1:buy peapock feathers' for row in rows)#any的意思是生成器表达式
        )
        #-------------------------------------------------------------------------------
        #页面还有一个输入框
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use tpeacock feathers to make a  fly')
        # 页面显示输入的内容,只是缓存
        inputbox.send_keys(Keys.ENTER)
        #table = self.browser.find_element_by_id('id_list_table')

        self.check_for_row_in_list_table('1:buy peapock feathers' )
        self.check_for_row_in_list_table('2:Use tpeacock feathers to make a  fly')

        # 生成制定的错误消息提醒测试结束
        self.fail('finished the test!')


    
if __name__ == '__main__':
    unittest.main()
