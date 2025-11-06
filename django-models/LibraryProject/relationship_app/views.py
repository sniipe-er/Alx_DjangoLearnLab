from django.shortcuts import render
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request):
    library = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html', {'library': library})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class UserCreationForm(request):
    model = UserCreationForm
    template_name = 'relationship_app/register.html'