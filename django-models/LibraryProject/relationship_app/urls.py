from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView, register
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('librarydetail/<int:pk>/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register.as_view(template_name='register.html'), name='register'),
]