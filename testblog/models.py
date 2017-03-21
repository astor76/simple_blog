from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)  # заголовок поста
    datetime = models.DateTimeField(verbose_name='Дата публикации')  # дата публикации
    content = models.TextField(max_length=10000)  # текст поста

    def __str__(self):  # возвращает строковое представление объекта
        return self.title

    def get_absolute_url(self):  # возвращает строку, которую можно использовать в HTTP запросе
        return "/blog/%i" % self.id


class Comment(models.Model):
    name = models.CharField(max_length=255)  # имя комментатора указывается при создании поста
    datetime = models.DateTimeField(verbose_name='Дата комментирования')  # дата комментирования
    content = models.TextField(max_length=1000)  # текст комментария


class Tag(models.Model):
    tagname = models.CharField(max_length=255)  # название тега


# Create your models here.
