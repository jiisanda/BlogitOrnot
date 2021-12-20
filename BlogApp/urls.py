from os import name
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView
from .views import BlogDeleteView, AddCategoryView
from BlogApp import views

# TEMPLATE URLS
urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('', BlogListView.as_view(), name="home"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:categ>/', views.CategoryView, name='category'),
]
