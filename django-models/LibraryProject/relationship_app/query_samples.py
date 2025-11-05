from models import *

books = Author.objects.get(name = author_name)
books = Book.objects.filter(author = author_name)
books = books.all()
library = Library.objects.get(name=library_name)
Librarian = Librarian.objects.get(library = library_name)
Library = Librarian.library