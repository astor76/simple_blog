#coding: utf-8
from django.conf.urls import url


from testblog.views import PostsListView, PostsDetailView, post_list


urlpatterns = (
    # url(r'^$', PostsListView.as_view(), name='list'),  # список постов выводится по URL http://имя_сайта/blog/
    url(r'^$', post_list, name='list'), # список постов выводится по URL http://имя_сайта/blog/
    url(r'^post/(?P<pk>\d+)/$', PostsDetailView.as_view()),  # конкретный пост выводится по URL http://имя_сайта/blog/число/
)
