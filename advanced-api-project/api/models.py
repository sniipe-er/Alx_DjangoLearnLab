from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateField()

    def __str__(self):
        return self.title
