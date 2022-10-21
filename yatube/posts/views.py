from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group
from django.shortcuts import redirect


COUNT = 10


def index(request):
    posts = Post.objects.all()[:COUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context=context)


def only_user_view(request):
    if not request.user.is_authenticated:
        # Если пользователь не авторизован - отправляем его на страницу логина.
        return redirect('/auth/login/')
    # Если пользователь авторизован — здесь выполняется полезный код функции.
