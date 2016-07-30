# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'superlists.settings'

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
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
        
        self.browser.get(self.live_server_url)#打开主页,软编码
        #网页的标题和头部都包含 todo
        self.assertIn('To-Do', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text()#网页的头部包含to-do,这句话是说明如何找头部的信息
        self.assertIn('To-Do', header_text)
        
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to do item')
        
        inputbox.send_keys('buy peapock feathers')
        #页面显示输入的内容,只是缓存
        inputbox.send_keys(Keys.ENTER)
        edith_list_all=self.browser.current_url#获取唯一的 url
        self.assertRegexp(edith_list_all,'/lists/.+')
        self.check_for_row_in_list_table('1:buy peapock feathers')
        
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
        # table = self.browser.find_element_by_id('id_list_table')
        inputbox.send_keys(Keys.ENTER)


        self.check_for_row_in_list_table('1:buy peapock feathers' )
        self.check_for_row_in_list_table('2:Use tpeacock feathers to make a  fly')

        # 生成制定的错误消息提醒测试结束
        #self.fail('finished the test!')


#不需要main 方法来运行测试了,只用 Django的manage.py 运行
#if __name__ == '__main__':
    #unittest.main()


        #启动一个新的浏览器会话
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        #检验用户B的输入项
        page_text=self.browser.find_element_by_tag_name('body').text#获取tage_name是body对应的值
        self.assertNotIn('buy peapock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #新用户A新建清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)

        francis_list_url=self.browser.current_url#在用户A输入buy milk后获得的 url
        self.assertRegexp(edith_list_all, '/lists/.+')
        self.assertNotEquals(francis_list_url,edith_list_all)#对比第一次生成的url和第二次生成的应该不同(url 不同是对的)

        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peapock feathers',page_text)#对比旧用户中应该不会出现新用户的输入项
        self.assertNotIn('buy milk',page_text)#断言检测正确的地方

