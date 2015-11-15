# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('team_name', models.CharField(max_length=255, unique=True, blank=True, default='')),
                ('organization', models.CharField(max_length=255, blank=True, default='')),
                ('email', models.EmailField(max_length=255)),
                ('problem_num', models.IntegerField(blank=True, null=True, default=0)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('language', models.CharField(max_length=255, default='ja')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', blank=True, verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', blank=True, verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'ordering': ['created_at'],
                'verbose_name': 'Team',
            },
        ),
    ]
