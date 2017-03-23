#coding: utf-8
from django.http import Http404
from django.shortcuts import render
from testblog.models import Post, Comment, Tag


def posts_list_view(request):
    """
    Отображение списка постов
    """
    ctx = {
        'title': 'Список постов',
        'post_list': Post.objects.all(),
    }
    return render(request, 'testblog/post_list.html',  ctx)
# Останется задать данному представлению url правило и готово!
# https://docs.djangoproject.com/en/1.10/intro/tutorial03/#a-shortcut-render


def post_detail(request, post_id):
    """
    Вывод одного поста
    """
    try:
        selectionpost = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    ctx = {
        'title': 'Просмотр поста',
        'post': selectionpost,
        # 'comments': Comment.objects.all(),
        # 'comments': Comment.objects.filter(boundpost=Post),
        # 'tag': Post.boundedtag,
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


def search_result(request, tag_name):
    """
    Страница поисковой выдачи
    """
    try:
        selectiontag = Tag.objects.get(tagname=tag_name)
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")
    ctx = {
        'title': 'Поиск постов',
        'search_tag': selectiontag,
        # 'post_list': Post.objects.all(),
        'post_list': Post.objects.filter(boundedtag=selectiontag),
    }
    return render(request, 'testblog/search_result.html', ctx)


def add_new_post(request):
    """
    Страница добавления нового поста
    """
    if request.method == 'POST':
        new_tag = Tag.objects.get_or_create(tagname=request.POST['tagname'])
        # new_tag = Tag.objects.get_or_create(tagname='добавленныйтег')
        new_post = Post.objects.create(title=request.POST['title'],
                                       content=request.POST['content'], boundedtag=new_tag)
        new_post.save()
        new_tag.save()
    return render(request, 'testblog/add_post.html')

# Create your views here.
