from django.shortcuts import render
from .models import Notes

# Create your views here.
def editor(request):
    notesid = int(request.GET.get('notesid', 0))
    notes = Notes.objects.all()
    context={
        'notesid':notesid,
        'notes':notes,
    }
    return render(request, 'notes/editor.html', context)
