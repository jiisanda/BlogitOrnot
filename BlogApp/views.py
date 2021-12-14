from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from BlogApp.forms import UserForm, UserProfileInfoForm

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name='BlogApp\home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'BlogApp\post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'BlogApp\post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "BlogApp\post_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "BlogApp\post_delete.html"
    success_url = reverse_lazy('home')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('if_not_login'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone try to logon and failed...")
            print("User: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'BlogApp/login.html', {})

def IfNotLoginView(request):
    return render(request, 'BlogApp\if_not_login.html')


def registrationView(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'BlogApp/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

