from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books', null=True, blank=True)


    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']
