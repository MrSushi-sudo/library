from django.test import TestCase
from ..views import *


class AuthorBookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Тестовый Автор 1')
        test_book = Book.objects.create(name='Тестовая Книга 1', description='Тестовое описание 1')
        test_book.authors.set('1')

    def test_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_book_authors_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('authors').verbose_name
        self.assertEquals(field_label, 'authors')

    def test_author_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_description_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('description').max_length
        self.assertEquals(max_length, 400)

    def test_object_name_is_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = '%s, %s' % (book.name, book.description)
        self.assertEquals(expected_object_name, str(book.name + ', ' + book.description))



