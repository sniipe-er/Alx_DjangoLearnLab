from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list_books', views.list_books, name = 'list_books'),
    path('library_details', views.library_details, name = 'library_details')
]