from django.shortcuts import render, get_object_or_404
from .models import Post, Group


COUNT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:COUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    f'записи{slug}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:COUNT]
    context = {
        'page_title: page_title,'
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context=context)
