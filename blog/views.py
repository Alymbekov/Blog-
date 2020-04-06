from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogPostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'


class BlogPostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/blog_post_edit.html'
    fields = ('title', 'body')


class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('index')