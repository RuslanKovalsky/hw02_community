from django.contrib import admin
from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    empty_value_display = 'пусто'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
# Для настройки отображения модели в интерфейсе
# админки применяют класс ModelAdmin. Он связывается с
# моделью и конфигурирует отображение данных этой модели
