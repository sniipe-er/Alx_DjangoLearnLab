from .models import *

author = Author.objects.get(name = '')
books = Book.objects.get(author)
books = Book.objects.all()