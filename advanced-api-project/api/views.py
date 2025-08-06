from django_filters import rest_framework
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# --------------------------
# Generic Views for Book
# --------------------------

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all Book instances.
    Public access allowed.

    Supports:
    - Filtering: title, author, publication_year
    - Searching: title, author__name
    - Ordering: title, publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed for partial text search
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book instance by ID.
    Public access allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class InvalidUpdateRoute(APIView):
    """
    Placeholder view for invalid update route.
    Returns a 400 Bad Request.
    """
    def get(self, request, *args, **kwargs):
        return Response(
            {"detail": "Invalid route for update."},
            status=status.HTTP_400_BAD_REQUEST
        )

class InvalidDeleteRoute(APIView):
    """
    Placeholder view for invalid delete route.
    Returns a 400 Bad Request.
    """
    def get(self, request, *args, **kwargs):
        return Response(
            {"detail": "Invalid route for delete."},
            status=status.HTTP_400_BAD_REQUEST
        )