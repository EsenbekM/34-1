from django.shortcuts import render, redirect
from django.db.models import Q
from post.models import Post, HashTag, Comment
from post.forms import PostCreateForm, PostCreateForm2
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# CBV - Class Based View
# FBV - Function Based View
# PEP8 - Python Enhancement Proposal 8
# snake_case, CamelCase


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class PostListView(ListView):
    model = Post
    # template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.all()

        search = self.request.GET.get('search')
        if search:
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        return posts


# def posts_view(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()  # QuerySet
#         # SELECT * FROM post_post;
#
#         search = request.GET.get('search')
#         order = request.GET.get('order')
#
#         if search:
#             # posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)
#             posts = posts.filter(
#                 Q(title__icontains=search) |
#                 Q(content__icontains=search)
#             )
#
#         if order == 'title':
#             posts = posts.order_by('title')
#         elif order == '-title':
#             posts = posts.order_by('-title')
#         elif order == 'created_at':
#             posts = posts.order_by('created_at')
#         elif order == '-created_at':
#             posts = posts.order_by('-created_at')
#
#         max_page = posts.__len__() / settings.PAGE_SIZE
#         # 7 posts / 3 = 2.3333333333333335
#         # if 2.3333333333333335 < 2:
#         #     max_page = 2
#         if round(max_page) < max_page:
#             max_page = round(max_page) + 1
#         else:
#             max_page = round(max_page)
#
#         # posts = [post1, post2, post3, post4, post5, post6, post7]
#
#         # example: page = 1, PAGE_SIZE = 3
#         # (1 - 1) * 3 = 0
#         # 1 * 3 = 3
#         # posts[0:3]
#
#         # example: page = 2, PAGE_SIZE = 3
#         # (2 - 1) * 3 = 3
#         # 2 * 3 = 6
#         # posts[3:6]
#
#         # Formulas:
#         # start = (page - 1) * PAGE_SIZE
#         # end = page * PAGE_SIZE
#
#         page = int(request.GET.get('page', 1))
#
#         start = (page - 1) * settings.PAGE_SIZE
#         end = page * settings.PAGE_SIZE
#
#         posts = posts[start:end]
#
#         context = {
#             "posts": posts,
#             "pages": range(1, max_page + 1)
#         }
#
#         return render(request, 'posts/posts.html', context=context)

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Helooooooo"
        return context


# def post_detail_view(request, post_id):
#     if request.method == 'GET':
#         try:
#             post = Post.objects.get(id=post_id)
#         except Post.DoesNotExist:
#             return render(request, 'errors/404.html')
#
#         context = {
#             "post": post
#         }
#
#         return render(request,
#                       'posts/post_detail.html',
#                       context)


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


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm2

    def get_success_url(self):
        return '/posts/'

    def form_valid(self, form):
        # cleaned_data = form.cleaned_data
        # form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # form.add_error()
        return super().form_invalid(form)


# def post_create(request):
#     if request.method == 'GET':
#         context = {
#             "form": PostCreateForm
#         }
#         return render(request, 'posts/create.html', context)
#     if request.method == 'POST':
#         form = PostCreateForm2(request.POST, request.FILES)
#         if form.is_valid():
#             Post.objects.create(**form.cleaned_data)
#             return redirect("/posts/")
#
#         context = {
#             "form": form
#         }
#
#         return render(request, 'posts/create.html', context)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    form_class = PostCreateForm2
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return f"/posts/{self.object.id}/"


# def post_update_view(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         return render(request, 'errors/404.html')
#
#     if request.method == 'GET':
#         context = {
#             "form": PostCreateForm2(instance=post)
#         }
#         return render(request, 'posts/update.html', context)
#
#     if request.method == 'POST':
#         form = PostCreateForm2(
#             request.POST,
#             request.FILES,
#             instance=post
#         )
#
#         if form.is_valid():
#             form.save()
#             return redirect(f'/posts/{post.id}/')
#
#         return render(
#             request,
#             'posts/update.html',
#             {"form": form}
#         )

