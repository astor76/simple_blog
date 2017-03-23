# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя коментирующего')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Дата комментирования')),
                ('content', models.TextField(max_length=1000, verbose_name='Содержание комментария')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('content', models.TextField(max_length=10000, verbose_name='Содержание поста')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=255, verbose_name='Тег')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='boundedtag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testblog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='boundedpost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testblog.Post'),
        ),
    ]
