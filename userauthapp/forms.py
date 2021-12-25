from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from BlogApp.models import Profile
from userauthapp.models import UserProfileInfo
from django.contrib.auth.forms import PasswordChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name' ,'username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site',)


class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name' ,'username', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta():
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserProfileEditForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['bio', 'profile_picture', 'portfolio_site', 'github_username', 'github_url', 'twitter_username', 'twitter_url', 'instagram_username', 'instagram_url', 'facebook_username', 'facebook_url']

        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Bio...', 'rows':4, 'cols':40}),
            'portfolio_site':forms.URLInput(attrs={'class':'form-control', 'placeholder':'Portfolio Site'}),
            'github_username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github Username'}),
            'github_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://github.com/username'}),
            'twitter_username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Twitter Username'}),
            'twitter_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://twitter.com/username'}),
            'instagram_username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Username'}),
            'instagram_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://instagram.com/username'}),
            'facebook_username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Username'}),
            'facebook_url':forms.URLInput(attrs={'class':'form-control', 'placeholder':'https://facebook.com/username'}),
        }
