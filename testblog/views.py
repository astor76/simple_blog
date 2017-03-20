#coding: utf-8

from django.shortcuts import render
from testblog.models import Post
from django.views.generic import ListView
from django.views.generic import DetailView

class PostsListView(ListView):
    model = Post

class PostsDetailView(DetailView):
    model = Post

# Create your views here.
