# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partialpoint',
            options={'verbose_name': '配点情報', 'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'verbose_name': '問題', 'ordering': ['number']},
        ),
    ]
