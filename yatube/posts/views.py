from django.shortcuts import render, get_object_or_404
from .models import Post, Group


COUNT = 10


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:COUNT]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'template', context=context)
