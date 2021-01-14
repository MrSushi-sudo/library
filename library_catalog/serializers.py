from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        ordering = ['-id']
        model = Book
        fields = ('id', 'name', 'description', 'authors')


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Author
        fields = ('id', 'name', 'books')




