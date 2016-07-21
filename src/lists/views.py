# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse


def home_page(request):
    #request是请求的对象(就是用户的输入值),home.html 是渲染的模板名称, Django会根据模板的内容构建一个 HttpResponse 对象
    return render(request,'home.html',{'new_item_text':request.POST['item_text', '']})