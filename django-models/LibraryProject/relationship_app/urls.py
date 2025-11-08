from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('librarydetail/<int:pk>/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]