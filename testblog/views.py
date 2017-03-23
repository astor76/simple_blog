#coding: utf-8

from django.shortcuts import render
from testblog.models import Post, Comment, Tag
from django.views.generic import ListView
from django.views.generic import DetailView


def PostsListView(request):
    """
    Отображение списка постов
    """
    ctx = {
        'title': 'Список постов',
        'posts': Post.objects.all(),  # здесь не должно быть post_list ?
    }
    return render(request, 'testblog/post_list.html',  ctx)
# Останется задать данному представлению url правило и готово!
# https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render


def post_detail(request):
    """
    Вывод одного поста
    """
    ctx = {
        'title': 'Просмотр поста',
        'post': Post.objects.filter(Post.id),
        # 'tag': Post.boundedtag,
        'comments': Comment.objects.all(),
        # 'comments': Comment.objects.filter(boundpost=Post),
    }
    return render(request, 'testblog/post_detail.html', ctx)


def search_form(request):
    """
    Страница со всеми тегами
    """
    ctx = {
        'title': 'Поиск постов по тегу',
        'tag_list': Tag.objects.all(),
    }
    return render(request, 'testblog/search_form.html', ctx)


def search_result(request):
    """
    Страница поисковой выдачи
    """
    ctx = {
        'title': 'Поиск постов',
        'search_tag': Tag,
        'post_list': Post.objects.all(),
        # 'post_list': Post.objects.filter(boundedtag=Tag),
    }
    return render(request, 'testblog/search_result.html', ctx)


def add_post(request):
    """
    Страница добавления нового поста
    """
    return render(request, 'testblog/add_post.html')


# class PostsListView(ListView):
#     model = Post
#
#
# class PostsDetailView(DetailView):
#     model = Post

# Create your views here.
