from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render
from BlogApp.forms import PostForm, UpdateForm

from .models import Post, Category


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name='BlogApp\home.html'
    categ = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'BlogApp\post_detail.html'

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'BlogApp\post_new.html'
    # fields = '__all__'  ---- form_class is doin' all...


class BlogUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "BlogApp\post_edit.html"
    # fields = ['title', 'body']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(BlogUpdateView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "BlogApp\post_delete.html"
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = "BlogApp\category.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

def CategoryView(request, categ):
    category_post = Post.objects.filter(category=categ.replace('-',' '))
    return render(request, 'BlogApp\categories.html', {'categ':categ.title().replace('-',' '), 'category_post':category_post})

def CategoryListView(request, categ):
    categ_menu = Category.objects.all()
    return render(request, 'BlogApp\category_list.html', {'categ_menu':categ_menu})

