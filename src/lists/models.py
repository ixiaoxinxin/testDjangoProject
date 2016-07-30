# -*- coding: utf-8 -*-
from django.db import models

# 给 item类提供 save 方法

#python 顺序执行的, List 方法必须卸载前面,否则迁移无法执行成功
class List(models.Model):
    pass



class Item(models.Model):
    #text=models.TextField(default='')#给列的值添加默认值
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)#添加list和item的关系:应该是包含关系


