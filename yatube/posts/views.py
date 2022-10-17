from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    number_posts = Post.objects.filter(author=author).count()
    post_list = Post.objects.filter(author=author).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
        'number_posts': number_posts
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post_info = get_object_or_404(Post, pk=post_id)
    author_posts = post_info.author
    author_count = post_info.author.posts.count()
    context = {
        'post_info': post_info,
        'author_posts': author_posts,
        'author_count': author_count
    }
    return render(request, 'posts/post_detail.html', context)

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
