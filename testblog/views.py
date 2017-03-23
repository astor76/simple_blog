#coding: utf-8

from django.shortcuts import render
from testblog.models import Post, Comment, Tag
from django.views.generic import ListView
from django.views.generic import DetailView

def post_list(request):
    """
    Отображение списка постов
    """
    ctx = {
        'title': 'Список постов',
        'posts': Post.objects.all(),  # здесь не должно быть post_list ?
    }
    return render(request, './testblog/post_list.html',  ctx)
# Останется задать данному представлению url правило и готово!
# https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render

def post_detail(request):
    """
    Вывод одного поста
    """
    ctx = {
        'title': 'Просмотр поста',
        'post': Post,
        'comment_list': Comment.objects.filter(boundpost=Post),
    }
    return render(request, './testblog/post_detail.html', ctx)


def search_form(request):
    """
    Страница поиска
    """
    ctx = {
        'title': 'Поиск постов',
        'search_tag': Tag,
        'post_list': Post.objects.filter(boundedtag=Tag),
    }
    return render(request, './testblog/search_form.html', ctx)

class PostsListView(ListView):
    model = Post

class PostsDetailView(DetailView):
    model = Post

# Create your views here.
