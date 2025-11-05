from models import *

books = Book.object.filter(author_name="")
books = Library.books.all()
Librarian = Librarian.objects.get(name = "")
Library = Librarian.library