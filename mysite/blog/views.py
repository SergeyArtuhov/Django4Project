from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator

from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # постраничная разбивка с 3 постами на страницу
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    """
    Функция-представление деталей поста

    Аналог функции без использования get_objects_or_404()
    try:
        post = Post.publish.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No post found")

    :param request:
    :param id:
    :return:
    """

    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, "blog/post/detail.html", {"post": post})
