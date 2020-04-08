from django.urls import path
from .views import BlogSignUpView

urlpatterns = [
    #url для регистрации
    path('signup/', BlogSignUpView.as_view(), name='signup'),
]
