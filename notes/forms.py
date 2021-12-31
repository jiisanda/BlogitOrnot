from django import forms
from django.forms import widgets
from .models import Notes

class NoteForm(forms.Form):
    class Meta():
        model = Notes
        fields = ('user', 'title', 'note_content')

        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user', 'type':''}),
            'title':forms.TextInput(),
            'note_content':forms.Textarea(),
        }
