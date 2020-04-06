from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

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


