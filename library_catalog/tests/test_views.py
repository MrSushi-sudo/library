from rest_framework.test import APITestCase, APIRequestFactory
from ..views import *
from rest_framework.test import APIClient


class BookViewTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BookViewSet.as_view({'get': 'list'})
        self.url = '/api/books/'

    def test_get(self):
        self.client = APIClient()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        params = {'name': 'Тестовая Книга 1', 'description': 'Тестовое описание 1'}
        response = self.client.post(self.url, params)
        self.assertEqual(response.status_code, 201)


class AuthorViewTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BookViewSet.as_view({'get': 'list'})
        self.url = '/api/authors/'

    def test_get(self):
        self.client = APIClient()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        params = {'name': 'Тестовый Автор 1'}
        response = self.client.post(self.url, params)
        self.assertEqual(response.status_code, 201)
