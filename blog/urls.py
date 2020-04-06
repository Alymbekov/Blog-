from django.urls import path
from .views import BlogListView, BlogDetailView, BlogPostCreateView

urlpatterns = [
    path('blog/post/new/', BlogPostCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='index'),
]

#http://localhost:8000/blog/post/2/

#http://localhost:8000/