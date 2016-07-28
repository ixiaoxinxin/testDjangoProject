# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=None, verbose_name=lists.models.List),
        ),
    ]
