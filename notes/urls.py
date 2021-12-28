from django.urls import path
from notes import views

urlpatterns = [
    path('add-notes/', views.editor, name="add_notes"),
    path('delete-note/<int:notesid>/',views.DeleteNotesView, name='delete_note'),
]

