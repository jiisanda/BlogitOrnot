from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from BlogApp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name' ,'username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_picture')