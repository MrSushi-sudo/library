from rest_framework import viewsets
from rest_framework import filters
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('api/')
    return response


class AuthorViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
