from .models import Posts
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Posts.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Posts,
                             id=id, status=Posts.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})