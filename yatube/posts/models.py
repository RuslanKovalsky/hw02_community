from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model

User = get_user_model()


# Классы, с которыми работает ORM, называются моделями
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=400)

    def __str__(self) -> str:
        return str(self.title)


# Тип поля: DateTimeField, для хранения даты и времени;
# параметр auto_now_add определяет, что в поле будет автоматически
# подставлено время и дата создания новой записи
# Описание модели начинается с объявления:
# класс Post — это наследник класса Model из модуля models.
class Post(models.Model):
    text = models.TextField()
    # TextField — поле для хранения произвольного текста.
    pub_date = models.DateTimeField(auto_now_add=True)
    # DateTimeField — поле для хранения даты и времени.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
# Параметр on_delete=models.CASCADE обеспечивает связность данных
# таблицы User будет удалён пользователь, то будут удалены
# все связанные с ним посты.

    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='group'
    )
# Так, для модели Post в базе данных
# будет создана таблица с колонками text,
# pub_date и author, причём в колонке
# author должны быть указаны primary keys
# записей из таблицы User.
# Для полей в моделях указывают типы данных,
# соответствующие типам данных в БД.
# В коде модели Post описаны поля:
# TextField — поле для хранения произвольного текста.
# DateTimeField — поле для хранения даты и времени.
# Существуют похожие типы для хранения даты (DateField),
# промежутка времени (DurationField), просто времени (TimeField).
# ForeignKey — поле, в котором указывается ссылка на другую
# модель, или, в терминологии баз данных, ссылка на другую
# таблицу, на её primary key (pk). В нашем случае это ссылка
# на модель User. Это свойство обеспечивает связь (relation)
# между таблицами баз данных.
# Параметр on_delete=models.CASCADE обеспечивает связность
# данных: если из таблицы User будет удалён пользователь,
# то будут удалены все связанные с ним посты.
