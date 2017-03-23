from django.contrib import admin
from testblog.models import Post
from testblog.models import Comment
from testblog.models import Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)


# Register your models here.
