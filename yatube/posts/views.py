from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


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
