from bookshelf.models import Book
book = book.object.get("Nineteen Eighty-Four")
book.delete()
book.object.all()
#deleted succsessfully