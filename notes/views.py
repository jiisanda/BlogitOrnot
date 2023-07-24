from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from .models import Notes
from notes.forms import NoteForm
from notes.models import Notes

# Create your views here.
class Editor(View, LoginRequiredMixin):
    template_name = 'notes\editor.html'

    def get(self, request):
        notes_id = int(request.GET.get('notesid', 0))
        notes = Notes.objects.filter(user=request.user)
        note = Notes.objects.get(pk=notes_id) if notes_id > 0 else ''

        context = {
            'notesid':notes_id,
            'notes':notes,
            'note':note,
        }

        return render(request, 'notes/editor.html', context)

    def post(self, request):
        user=request.user
        notes_id = int(request.POST.get('notesid', 0))
        title=request.POST.get('title')
        note_content=request.POST.get('note_content', '')

        if notes_id > 0:
            note=Notes.objects.get(pk=notes_id)
            note.user = user
            note.title=title
            note.note_content=note_content
            note.save()

        else:
            note=Notes.objects.create(user=user, title=title, note_content=note_content)

        return HttpResponseRedirect(request.path_info) 


def DeleteNoteView(request, notes_id):
    note = Notes.objects.get(pk=notes_id)
    note.delete()
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)
