from .models import *

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
books = books.all()
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
library_from_librarian = librarian.library

# from models import *

# books = Author.objects.get(name = author_name)
# books = Book.objects.filter(author = author)
# books = books.all()
# library = Library.objects.get(name=library_name)
# Librarian = Librarian.objects.get(library = library_name)
# Library = Librarian.library