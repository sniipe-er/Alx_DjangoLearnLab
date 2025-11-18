from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class CustomUserManager(BaseUserManager):
    create_user = CustomUser.objects.create_user
    create_superuser = CustomUser.objects.create_superuser