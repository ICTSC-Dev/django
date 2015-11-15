# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartialResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('is_public', models.BooleanField(default=False)),
                ('add_pont', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('partialpoint', models.ForeignKey(to='problem.PartialPoint')),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'PartialResult',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('problem', models.ForeignKey(to='problem.Problem')),
                ('team', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Result',
            },
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('is_public', models.BooleanField(default=False)),
                ('add_pont', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, auto_now=True)),
                ('problem', models.ForeignKey(to='problem.Problem')),
                ('team', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Submit',
            },
        ),
        migrations.AddField(
            model_name='partialresult',
            name='submit',
            field=models.ForeignKey(to='log.Submit'),
        ),
    ]
