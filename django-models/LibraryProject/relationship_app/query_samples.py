from .models import *

author = Author.objects.get(name = author_name)
books_by_author = Book.objects.filter(author = author)

books = Library.books.all()

library = Library.objects.get(name = library_name)
librarian = Librarian.objects.get(library=)