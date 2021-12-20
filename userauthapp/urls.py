from os import name
from django.urls import path
from userauthapp import views


# app_name="UserAuthApp"
# TEMPLATE URLS
urlpatterns = [
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.registrationView, name='register'),
]
