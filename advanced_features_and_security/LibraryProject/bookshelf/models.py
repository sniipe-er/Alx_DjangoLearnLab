from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)