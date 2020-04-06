from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

urlpatterns = [
    path('blog/post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog/post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog/post/new/', BlogPostCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='index'),
]
# http://localhost:8000/blog/post/<int:pk>/delete/
#http://localhost:8000/blog/post/2/edit/
#http://localhost:8000/blog/post/2/ detail view
#http://localhost:8000/ list view