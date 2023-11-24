from django.shortcuts import HttpResponse, render

from post.models import Post, HashTag, Comment

# CBV - Class Based View
# FBV - Function Based View
# PEP8 - Python Enhancement Proposal 8
# snake_case, CamelCase


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()  # QuerySet
        # SELECT * FROM post_post;

        context = {
            "posts": posts,
        }

        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {
            "post": post
        }

        return render(request,
                      'posts/post_detail.html',
                      context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        context = {
            "hashtags": hashtags,
            "name": "Asyl"
        }

        return render(
            request,
            'posts/hashtags.html',
            context=context
        )
