import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    Executes various sample queries to demonstrate model relationships.
    """
    print("--- Running Sample Queries ---")

    # --- Create some sample data (if not already present) ---
    print("\nCreating sample data...")
    author1, created = Author.objects.get_or_create(name="Jane Austen")
    author2, created = Author.objects.get_or_create(name="George Orwell")

    book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
    book2, created = Book.objects.get_or_create(title="1984", author=author2)
    book3, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    book4, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)

    library1, created = Library.objects.get_or_create(name="City Central Library")
    library2, created = Library.objects.get_or_create(name="Community Read Library")

    if created: # Add books to libraries only if libraries were just created
        library1.books.add(book1, book2)
        library2.books.add(book3, book4)

    librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
    librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)

    print("Sample data created/ensured.")

    # --- Query all books by a specific author ---
    print("\n--- Query: All books by a specific author (George Orwell) ---")
    try:
        specific_author = Author.objects.get(name="George Orwell")
        books_by_author = specific_author.books.all() # Using the related_name 'books'
        if books_by_author:
            for book in books_by_author:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print(f"  No books found for {specific_author.name}.")
    except Author.DoesNotExist:
        print("  Author 'George Orwell' not found.")

    # --- List all books in a library ---
    print("\n--- Query: All books in 'City Central Library' ---")
    try:
        specific_library = Library.objects.get(name="City Central Library")
        books_in_library = specific_library.books.all()
        if books_in_library:
            for book in books_in_library:
                print(f"  - {book.title}")
        else:
            print(f"  No books found in {specific_library.name}.")
    except Library.DoesNotExist:
        print("  Library 'City Central Library' not found.")

    # --- Retrieve the librarian for a library ---
    print("\n--- Query: Librarian for 'Community Read Library' ---")
    try:
        specific_library = Library.objects.get(name="Community Read Library")
        # Accessing the librarian through the related_name 'librarian'
        librarian_for_library = specific_library.librarian
        print(f"  The librarian for {specific_library.name} is {librarian_for_library.name}.")
    except Library.DoesNotExist:
        print("  Library 'Community Read Library' not found.")
    except Librarian.DoesNotExist:
        print(f"  No librarian found for {specific_library.name}.")

if __name__ == '__main__':
    run_queries()