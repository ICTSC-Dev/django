# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partialresult',
            options={'verbose_name': '配点結果', 'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': '採点記録', 'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='submit',
            options={'verbose_name': '提出記録', 'ordering': ['-updated_at']},
        ),
    ]
