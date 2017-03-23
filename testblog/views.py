#coding: utf-8

from django.shortcuts import render
from testblog.models import Post
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Post

def post_list(request):
    """
    Отображение списка постов
    """
    ctx = {
        'title': 'Список постов',
        'posts': Post.objects.all(),
    }
    return render(request, './testblog/post_list.html',  ctx)
# Останется задать данному представлению url правило и готово!
# https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render

def search_tag(request):
    """
    Поиск по тегу
    """
    ctx = {
        'title': 'Поиск постов',

    }

class PostsListView(ListView):
    model = Post

class PostsDetailView(DetailView):
    model = Post

# Create your views here.
