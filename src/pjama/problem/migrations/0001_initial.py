# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartialPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'PartialPoint',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_point', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('fix_num', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Problem',
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='partialpoint',
            name='problem',
            field=models.ForeignKey(to='problem.Problem'),
        ),
    ]
