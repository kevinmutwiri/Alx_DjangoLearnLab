from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields and validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes the author's name and a nested list of related books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # 'books' is the related_name on Book.author

    class Meta:
        model = Author
        fields = ['name', 'books']
