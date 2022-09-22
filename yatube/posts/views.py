from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# COUNT_POST: int = 10
# вычитал на форуме что можно так сделать через каунт ...


def index(request):
    # по классике главная страница
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    page_title = 'last refreshed'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблонc
    context = {
        'page_title': page_title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Страничка где лежат списки сообществ
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    template = 'base/index.html'
    group = get_object_or_404(Group, slug=slug)
    page_title = f'записи{slug}'
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'page_title': page_title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
