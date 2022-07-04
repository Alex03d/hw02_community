from django.shortcuts import render, get_object_or_404

from .models import Post, Group


CONSTANT = 10


def index(request):
    posts = Post.objects.all().select_related('group', 'author')[:CONSTANT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:CONSTANT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
