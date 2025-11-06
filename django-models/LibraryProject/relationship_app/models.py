from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    Author = models.ForeignKey(Author)
    def __str__(self):
        return self.title