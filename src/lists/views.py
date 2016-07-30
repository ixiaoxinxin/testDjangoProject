# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from models import Item,List

def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/'%(new_list.id,))


def add_item(request,list_id):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_id.id,))


def view_list(request,list_id):
    list_ = List.objects.create(id=list_id)
    return render(request,'list.html',{'list':list_})



