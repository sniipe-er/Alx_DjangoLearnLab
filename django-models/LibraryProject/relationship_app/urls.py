from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books', views.list_books, name = 'list_books'),
    path('library_details', views.library_details, name = 'library_details'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout')
]