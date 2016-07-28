# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from models import Item,List
from views import home_page

#每个测试用例中的所有方法
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        #resolve是解析主页的域名
        found=resolve('/')
        self.assertEqual(found.func, home_page)
    #以上代码的意思是:用 resolve 解析(并将其映射到相应的视图函数)根目录的时候最后能找到名为 home_page 的函数(在 view 文件中找)


    def test_home_page_returns_correct_html(self):
        requset = HttpRequest()#用于存储用户在浏览网页的时候请求的对象
        response = home_page(requset)# 将用户浏览网页时的内容传给视图,通过视图得到相应
        #--------------------以下是测试 request的返回值(功能测试)------------------------------
        self.assertTrue(response.content.startswith(b'<html>'))#使用 content.startswith()是原始字节,对比的时候要用 b''
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endwith(b'</html>'))

    #def test_home_page_can_save_a_POST_request(self):#将post 请求的结果,即生成的提交数据库存储到数据库中



        #self.assertEqual(resopnse.status_code,302)#其中3XX的代码都用来重定向,302的意思是服务器从不同位置的网页相应请求
        #self.assertEqual(resopnse['location'],'/')


        #self.assertIn('A new list item', resopnse.content.decode())
        #这个方法是处理 post 请求;请求的名称是'item_text',给"请求"赋值一个名称,并查看该请求的返回值
        #用render_to_string函数渲染模板,然后用这个渲染模板的返回值与试图函数 view.py的html做比较
        #expected_html = render_to_string(
            #'home.html',
           # {'new_item_text':'A new list item'}
        #)
        #第二个参数是变量名到值的映射,向模板中传入一个名为new_item_text的对象, A....的值是 post 发送的待办事项文本
        #self.assertEqual(resopnse.content.decode(), expected_html)
        #运行时候的效果:把 python 变量传入模板中将<table id="id_list_table"></table>这里的值渲染成'A new list item'


    #def test_home_page_only_saves_items_when_necessary(self):
        #request = HttpRequest()
        #home_page(request)
        #self.assertEqual(Item.objects.count(),0)#检验返回值是否是数据库中存的第一个值


    #def test_home_page_redirects_after_POST(self):




#-class ItemModelTest(TestCase):
class ListAndItemModelsTest(TestCase):


    def test_saving_and_retrieving_items(self):
        #执行步骤是:创建一个对象,赋值,调用.save 函数
        #new
        list_=List()
        list_.save()

        first_item=Item()
        first_item.text='The first(ever)list item'
        #---new---
        first_item.list-list_
        #---------
        first_item.save()

        second_item=Item()
        second_item.text='item the second'
        # ---new---
        second_item.list - list_
        # ---------
        second_item.save()
        #-----new-----
        saved_list = List.objects.first()
        self.assertEqual(saved_list,list_)
        # ------------

        saved_items=Item.object.all()#取回表的全部记录
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        #new
        self.assertEqual(first_saved_item.list,list_)
        #----
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)#比较两个清单对象的.id 属性是否相同
        #将两个待办清单事项存数在list_中

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/list/the-only-list-in-the-world/')
        #将指定用户输入值作为 request, 提交后渲染home.html,
        # 输入的内容最终显示到 list.html
        self.assertTemplateUsed(response,'list.html')

    def test_display_all_items(self):
        list_=List.objects.create()
        Item.objects.create(text='itemy 1',list=list_)
        Item.objects.create(text='itemy 2',list=list_)

        response = self.client.get('/list/the-only-list-in-the-world/')

        self.assertContains(response,'itemy 1')
        self.assertContains(response, 'itemy 2')#assertContains知道如何处理响应和响应中的字节


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['item_text'] = 'A new list item'  #

        #resopnse = home_page(request)  # 没有调用response的包

        #self.assertEqual(Item.objects.count(), 1)
        #new_item = Item.objects.first()  # 初始化一个数组
        #self.assertEqual(new_item.text, 'A new list item')  # 查看文本是否正确


        #用Django 客户端重写这个方法:
        self.client.post(
            'list/new',#需要加入到 url 的映射中
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count,1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 1)

    def test_redirects_adter_POST(self):
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['item_text'] = 'A new list item'  # 模板中 input的 name
        respone = self.client.post(
            'lists/new',
            data={'item_text': 'A new list item'}
        )
        #self.assertEqual(respone.status_code, 302)这个重定向的检查会给 url 加上域名,所以去掉,下面的 response  location 去掉
        self.assertEqual(respone, '/lists/the-only-list-in-theworld/')



