from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers as hasher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from django.urls import reverse
from django.urls.base import reverse_lazy

from .forms import ProfileEditForm, UserProfileEditForm
from .models import Profile

from BlogApp.models import Post
from userauthapp.forms import UserForm, UserProfileInfoForm, PasswordChangingForm


# Create your views here
class UserLogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class UserLoginView(View):
    template_name = 'userauthapp/login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("Invalid login details supplied!")


class RegisterView(View):
    template_name = 'userauthapp/registration.html'

    registered = False

    def get(self, request):
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': self.registered,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # self._extracted_from_post(request, user_form=user_form, profile_form=profile_form)
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            self.registered = True
        else:
            print(user_form.errors, profile_form.errors)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': self.registered,
        }

        return render(request, self.template_name, context=context)


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

class ShowProfilePageView(generic.DetailView):
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
