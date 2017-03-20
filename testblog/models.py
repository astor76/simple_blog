from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)  # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации')  # дата публикации
    content = models.TextField(max_length=10000)  # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i" % self.id


class Comment(models.Model):
    name = models.CharField(max_length=255)  # имя комментатора указывается при создании поста
    datetime = models.DateTimeField(u'Дата комментирования')  # дата комментирования
    content = models.TextField(max_length=1000)  # текст комментария


class Tag(models.Model):
    tagname = models.CharField(max_length=255)  # название тега
# Create your models here.
