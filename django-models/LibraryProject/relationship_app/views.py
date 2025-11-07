from django.shortcuts import render
from .models import *
# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'book/book_list.html', context)