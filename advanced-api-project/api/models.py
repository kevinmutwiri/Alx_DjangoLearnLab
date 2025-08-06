from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Model representing a book author.
    - name: Stores the author's full name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: Foreign key linking to Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
