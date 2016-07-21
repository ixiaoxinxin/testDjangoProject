# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import resolve
from views import home_page
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

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

    def test_home_page_can_save_a_POST_request(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        resopnse=home_page(request)
        self.assertIn('A new list item', response.content.decode())
        #这个方法是处理 post 请求;请求的名称是'item_text',给"请求"赋值一个名称,并查看该请求的返回值
        #用render_to_string函数渲染模板,然后用这个渲染模板的返回值与试图函数 view.py的html做比较
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':'A new list item'}
        )
        #第二个参数是变量名到值的映射,向模板中传入一个名为new_item_text的对象, A....的值是 post 发送的待办事项文本
        self.assertEqual(response.content.decode(), expected_html)
        #运行时候的效果:把 python 变量传入模板中将<table id="id_list_table"></table>这里的值渲染成'A new list item'


