from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from notes.forms import NoteForm
from .models import Notes
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from notes.models import Notes

# Create your views here.
@login_required
def editor(request):
    notesid = int(request.GET.get('notesid', 0))
    notes = Notes.objects.filter(user=request.user)

    # form = NoteForm(request.POST)
    # if form.is_valid():
    if request.method == 'POST':
        notesid = int(request.POST.get('notesid', 0))
        title=request.POST.get('title')
        note_content=request.POST.get('note_content', '')

        if notesid > 0:
            note=Notes.objects.get(pk=notesid)
            note.title=title
            note.note_content=note_content
            note.save()

            # return redirect('/?notesid=%i' % notesid)
            return HttpResponseRedirect(request.path_info)
        
        else:
            note=Notes.objects.create(title=title, note_content=note_content)

            # return redirect('/?notesid=%i' % note.id)
            return HttpResponseRedirect(request.path_info) 

    if notesid > 0 :
        note = Notes.objects.get(pk=notesid)
    else:
        note = ''
    
    context={
        'notesid':notesid,
        'notes':notes,
        'note':note,
    }
    return render(request, 'notes/editor.html', context)


def DeleteNotesView(request, notesid):
    note = Notes.objects.get(pk=notesid)
    note.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
