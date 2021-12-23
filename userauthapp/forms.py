from django import forms
from django.contrib.auth.models import User
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