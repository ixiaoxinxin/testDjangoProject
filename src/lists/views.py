# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import Item


def home_page(request):
    if request.method=='POST':
        #new_item_text=request.POST['item_text']#将 post 也就是 home 对应的 item_text 值存到new_item_text这个变量中
        #Item.objects.create(text=new_item_text)#相当于.save 方法,存储数据使用
    #else:
        #new_item_text=''#item_text对应的值有可能是空的

        #return render(request, 'home.html', {'new_item_text': new_item_text})#
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    return render(request,'home.html')

