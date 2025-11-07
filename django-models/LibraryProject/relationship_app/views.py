from django.shortcuts import render
from .models import Book , Library
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

def library_detail(request):
    library = Library.objects.all()
    context = {'library_detail': library}
    return render(request, 'relationship_app/library_detail.html', context)