from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    list_filter = ('publication_year', 'author')

    search_fields = ('title', 'author')

    list_per_page = 25

admin.site.register(Book, BookAdmin)
