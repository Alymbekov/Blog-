from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
]

#http://localhost:8000/