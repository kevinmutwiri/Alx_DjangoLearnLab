from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author1)
        self.book2 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author2)

        self.book_list_url = reverse('book-list')
        self.book_create_url = reverse('book-create')

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Test Book",
            "publication_year": 2024,
            "author": self.author1.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_retrieve_single_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 1958,
            "author": self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.book_list_url + f'?author={self.author1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    def test_search_books_by_title(self):
        response = self.client.get(self.book_list_url + '?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.book_list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")  # 1997 > 1958
