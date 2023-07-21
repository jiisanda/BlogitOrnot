from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from userauthapp.forms import UserForm, UserProfileInfoForm, PasswordChangingForm
from django.views import generic
from .forms import ProfileEditForm, UserProfileEditForm
from django.views.generic import DetailView
from .models import Profile
from BlogApp.models import Post
import django.contrib.auth.hashers as hasher

# Create your views here


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

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
        return render(request, 'userauthapp/login.html', {})


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
    
    return render(request, 'userauthapp/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})


class ProfileEditView(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'userauthapp/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # from_class = PasswordChangeForm
    template_name='userauthapp/change_password.html'
    success_url = reverse_lazy('password_changed')


def PasswordSuccessView(request):
    return render(request, 'userauthapp/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'userauthapp/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        blogs = Post.objects.all()

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        context["blogs"] = list(blogs)
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = UserProfileEditForm
    template_name = 'userauthapp/edit_user_profile.html'
    # fields = ['bio', 'profile_picture', 'portfolio_site', 'github_username', 'github_url', 'twitter_username', 'twitter_url', 'instagram_username', 'instagram_url', 'facebook_username', 'facebook_url']
    
    success_url = reverse_lazy('home')

    