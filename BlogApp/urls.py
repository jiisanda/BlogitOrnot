from os import name
from typing import Pattern
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, SearchResultsView, AddCategoryView
from BlogApp import views

# TEMPLATE URLS
urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('', BlogListView.as_view(), name="home"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.registrationView, name='register'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
