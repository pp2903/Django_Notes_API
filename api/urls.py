from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/create', views.createNote, name="create-note"),
    path('note/<int:pk>/update', views.updateNote, name="update-note"),
    path('note/<int:pk>', views.getNote, name="note"),
    path('note/<int:pk>/delete', views.deleteNote, name="delete-note"),
]
