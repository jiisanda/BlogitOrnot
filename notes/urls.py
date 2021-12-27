from django.urls import path
from notes import views

urlpatterns = [
    path('add-notes/', views.editor, name="add_notes"),
]

