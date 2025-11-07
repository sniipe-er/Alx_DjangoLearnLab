from django.shortcuts import render
from .models import Library
from .models import *
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class library_detail(models.Model):
    library = Library.objects.all()
    context = {'library_detail': library}
    render(library, 'relationship_app/library_detail.html', context)