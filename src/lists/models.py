# -*- coding: utf-8 -*-
from django.db import models

# 给 item类提供 save 方法
class Item(models.Model):
    text=models.TextField(default='')#给列的值添加默认值
