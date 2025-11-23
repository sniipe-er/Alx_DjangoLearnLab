from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(generics.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer