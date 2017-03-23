from django.db import models


class Tag(models.Model):
    tagname = models.CharField(verbose_name='Содержание тега', max_length=255)  # название тега

    def __str__(self):  # возвращает строковое представление объекта
        return self.tagname

    # def get_bounded_posts(self):
    #     bounded_posts = Post.objects.filter(tagpost=self)
    #     # так вообще можно делать? нужно вернуть коллекцию постов
    #     return bounded_posts


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок поста', max_length=255)  # заголовок поста
    datetime = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)  # дата публикации
    content = models.TextField(verbose_name='Содержание поста', max_length=10000)  # текст поста
    boundedtag = models.ForeignKey(Tag, to_field=Tag.tagname)  # связанный тег поста, связь много-к-одному

    def __str__(self):  # возвращает строковое представление объекта
        return self.title

    def get_absolute_url(self):  # возвращает строку, которую можно использовать в HTTP запросе
        return "/blog/%i" % self.id

    # def get_bounded_comments(self):  # получить все связанные с постом комменты
    #     bounded_comments = Comment.objects.filter(boundpost=self)
    #     # так вообще можно делать? нужно вернуть коллекцию комментариев
    #     return bounded_comments


class Comment(models.Model):
    name = models.CharField(verbose_name='Имя коментирующего', max_length=255)  # имя комментатора
    datetime = models.DateTimeField(verbose_name='Дата комментирования', auto_now=True)  # дата комментирования
    content = models.TextField(verbose_name='Содержание комментария', max_length=1000)  # текст комментария
    boundedpost = models.ForeignKey(Post, to_field=id(Post))  # связанный тег поста, связь много-к-одному

# Create your models here.

# # примеры кода для работы с моделями
# # создание тега
# MyTag = Tag.objects.create(tagname='Зима близка!')
# MyTag.save()
# # Создание поста и привязка к тега
# MyPost = Post.objects.create(title='Заголовок поста', content='Пример текста поста', boundedtag=MyTag)
# MyPost.save()
# # создание комментариев и привязка к посту
# MyComment1 = Comment.objects.create(name='Alex', content='Одичалые толпятся у стены', boundpost=MyPost)
# MyComment1.save()
# MyComment2 = Comment.objects.create(name='Alex', content='Белые ходоки собирают армию', boundpost=MyPost)
# MyComment2.save()
#
# # выбор всех комментариев к посту MyPost
# Comment.objects.filter(boundpost=MyPost)
# # выбор всех постов с тегом MyTag
# Post.objects.filter(tagpost=MyTag)
