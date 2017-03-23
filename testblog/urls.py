#coding: utf-8
from django.conf.urls import url


from testblog.views import *


urlpatterns = (

    url(r'addpost/', add_post, name='addpost'),  # страница добавления поста выводится по URL http://testsite/myblog/addpost/
    url(r'search/', search_form, name='searchform'),  # страница c поисковой формой выводится по URL http://testsite/myblog/search/
    url(r'^$', PostsListView, name='list'),  # список постов выводится по URL http://testsite/myblog/

    url(r'search/([_ \w]+)/', search_result, name='searchresult'),  # выдача поиска, http://testsite/myblog/search/"строка букв и _ "/

    url(r'(\d+)/', post_detail, name='postdetail'),  # конкретный пост выводится по URL http://testsite/myblog/число/
)


# url(r'^$', PostsListView.as_view(), name='list'),  # список постов выводится по URL http://имя_сайта/myblog/
# url(r'^(?P<pk>\d+)/$', PostsDetailView.as_view()),  # конкретный пост выводится по URL http://имя_сайта/myblog/число/
