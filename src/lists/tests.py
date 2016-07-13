# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http.request import HttpRequest
# Create your tests here.
#确认会失败的测试
#class SmokeTest(TestCase):
    #def test_bad_maths(self):
        #self.assertEqual(1+1, 3)
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func, home_page)
        
#以上代码的意思是:用 resolve 解析(并将其映射到相应的视图函数)根目录的时候最后能找到名为 home_page 的函数
    def test_home_page_returns_correct_html(self):
        requset = HttpRequest()#用于存储用户在浏览网页的时候请求的对象
        response = home_page(requset)# 将用户浏览网页时的内容传给视图,通过视图得到相应
        #--------------------以下是测试 request的返回值(功能测试)------------------------------#
        self.assertTrue(response.content.startswith(b'<html>'))#使用 content.startswith()是原始字节,对比的时候要用 b''
        self.assertIn(b'<title>To-Do list</title>', response.content)
        self.assertTrue(response.content.endwith(b'</html>'))