# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import Item,List


def home_page(request):
    #if request.method=='POST':
        #new_item_text=request.POST['item_text']#将 post 也就是 home 对应的 item_text 值存到new_item_text这个变量中
        #Item.objects.create(text=new_item_text)#相当于.save 方法,存储数据使用
    #else:
        #new_item_text=''#item_text对应的值有可能是空的

        #return render(request, 'home.html', {'new_item_text': new_item_text})#
        #Item.objects.create(text=request.POST['item_text'])
        #return redirect('/list/the-only-list-in-the-world/')#返回渲染好的模板页面


    #items = Item.objects.all()#将用户输入的待办事项传入模板
    #return render(request,'home.html',{'items':items})#来源,去向(渲染的模板),和传入的内容
    return render(request, 'home.html')


def view_list(request,list_id):
    list_ = List.objects.create(id=list_id)
    return render(request,'list.html',{'list':list_})

def new_list(request):#创建待办事项
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/'%(new_list.id,))#重定向到另外一个 url

def add_item(request,list_id):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)#让视图保存新的待办事项
    return redirect('/lists/%d/' % (list_id.id,))