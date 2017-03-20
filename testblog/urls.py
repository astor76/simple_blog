#coding: utf-8
from django.conf.urls import url


from testblog.views import PostsListView, PostsDetailView


urlpatterns = (
    url(r'^$', PostsListView.as_view(), name='list'),  # список постов выводится по URL http://имя_сайта/blog/
    url(r'^(?P<pk>\d+)/$', PostsDetailView.as_view()),  # конкретный пост выводится по URL http://имя_сайта/blog/число/
)
