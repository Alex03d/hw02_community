from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.Get.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


# NUMBER_OF_POSTS: int = 10


# def index(request):
#     posts = (
#         Post.objects.all().
#         select_related('group', 'author')[:NUMBER_OF_POSTS]
#     )
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
