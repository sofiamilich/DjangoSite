знеfrom django.db import models
from django.utils import timezone # часовые пояса
from django.contrib.auth.models import User # аудент.пользователя


# Описываем сами модели. Будем создавать таблицы с помощью данного класса

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'), # черновая публикация
        ('published', 'Published'), # не черновая публикация
    )
    title = models.CharField(max_length=250)# поле для текста, ограничено 250 симв
    #  создадим техническую переменную для хранения тех информации и генерации ссылки на пост
    slug = models.SlugField(max_length=250, unique_for_date='publish')   # отдельное поле, содержащее уникальную дату
    # создадим также автора поста, оно будет первичным ключом - опрделять будем по автору, так как статей м.б. много,
    # с передачей параметра - Пользователь, так как импортировали Юзера. А так же, если происходит удаление,
    # то - что удаляется
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='blog_posts')
    # добавим тело блога с обычным текстовым полем, не будем ограничивать параметрами
    body = models.TextField()
    # Создадим публикацию, в ней будет хранится дата и время
    publish = models.DateTimeField(default=timezone.now)
    #  Создадим дату создания статьи, так как есть не опубликованные, которые еще дописываются, в параметр будет
    #  подставляться - когда было применено изменение
    created = models.DateTimeField(auto_now_add=True)
    #  сделаем когда статья обновилась - с номером и датой
    updated = models.DateTimeField(auto_now=True)
    # Статус может быть только либо опубликова, либо нет, самостоятельно писать нельзя будет (чойсес - вариант выбора)
    # драфт - в качестве наброска
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)  #  сортировка по публикациям наоборот, чтобы самые свежие выходили сначала


    def __str__(self):
        return self.title #Возвращает отображение понятное человеку

