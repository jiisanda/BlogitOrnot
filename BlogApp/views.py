from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from BlogApp.forms import PostForm, UpdateForm, AddCommentForm

from .models import Comment, Post, Category


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
        # to know which post user is on
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])     # this says look up a post with an id and assign it to stuff
        total_likes = stuff.total_likes()   # take total_likes form the stuff which gets calculated form models.py 
        
        context["categ_menu"] = categ_menu
        context['total_likes'] = total_likes
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


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))    # here i am filling out the form
                                            # and submitting it and when submitting grabbing the post.id by request.POST.get
                                            # why post_id? bcz in post_detail.html the name of the button is it.
    post.likes.add(request.user)    # adding the user that liked the post as in "harsh liked the post by TheWhiteWolf"
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))  # args to know which blog post we are returning/redirecting

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'BlogApp/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        post_id=self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


    # success_url = reverse_lazy('post_detail')

class UserPostView(ListView):
    model = Post
    template_name = 'BlogApp/user_posts.html'

    def get_context_data(self, *args, **kwargs):
        user_post = Post.objects.all()
        context = super(UserPostView, self).get_context_data(*args, **kwargs)
        context["user_post"] = user_post
        # print(context)
        return context
