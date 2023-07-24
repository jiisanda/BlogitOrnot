from django.urls import path
from notes import views

urlpatterns = [
    path('notes/', views.Editor.as_view(), name="add_notes"),
    path('notes/<int:notes_id>/delete',views.DeleteNoteView, name='delete_note'),
]

