from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    page_title = 'last refreshed'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'page_title': page_title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    page_title = f'записи{slug}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'page_title': page_title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context=context)
