from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request):
    library = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html', {'library': library})
