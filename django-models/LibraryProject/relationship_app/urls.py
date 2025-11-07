from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('LibraryDetailView', views.library_detail, name='LibraryDetailView')
]