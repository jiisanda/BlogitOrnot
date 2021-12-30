from django import forms
from django.forms import widgets
from BlogApp.models import Comment, Post, Category

# choices = [('Coding', 'Coding'), ('Entertainment', 'Entertainment'), ('Education', 'Education')]
choices = Category.objects.all().values_list('name', 'name')

choices_list =[]
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'writer', 'category', 'body', 'post_date', 'post_picture')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the blog...'}),
            # 'writer': forms.Select(attrs={'class':'form-control'}),
            'writer': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer_name', 'type':'hidden'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body of the Blog...'}),
            'post_date': forms.DateInput(),   
            # 'post_picture': forms.ImageField(),
        }


class UpdateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'body', 'category','post_date', 'post_picture')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the blog...'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body of the Blog...'}),
            'post_date': forms.DateInput(),   
            # 'post_picture': forms.ImageField(),
        }


class AddCommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('comment_name', 'comment_body')

        widgets = {
            'comment_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
            'comment_body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment...'}),
        }
