from .models import *

author = Author.objects.get(name = author_name)
books = Book.objects.get(author)
books = Book.all()
library = Library.objects.get(name = library_name)