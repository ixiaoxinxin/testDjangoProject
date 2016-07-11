# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
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