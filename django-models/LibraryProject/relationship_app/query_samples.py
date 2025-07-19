import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Running Sample Queries ---")

    print("\nCreating sample data...")
    author1, created = Author.objects.get_or_create(name="Jane Austen")
    author2, created = Author.objects.get_or_create(name="George Orwell")

    book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
    book2, created = Book.objects.get_or_create(title="1984", author=author2)
    book3, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    book4, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)

    library1, created = Library.objects.get_or_create(name="City Central Library")
    library2, created = Library.objects.get_or_create(name="Community Read Library")

    if created:
        library1.books.add(book1, book2)
        library2.books.add(book3, book4)

    librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
    librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)

    print("Sample data created/ensured.")

    print("\n--- Query: All books by a specific author (George Orwell) ---")
    try:
        author_name = "George Orwell"
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        if books_by_author:
            for book in books_by_author:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print(f"  No books found for {author.name}.")
    except Author.DoesNotExist:
        print(f"  Author '{author_name}' not found.")

    print("\n--- Query: All books in 'City Central Library' ---")
    try:
        library_name = "City Central Library"
        specific_library = Library.objects.get(name=library_name)
        books_in_library = specific_library.books.all()
        if books_in_library:
            for book in books_in_library:
                print(f"  - {book.title}")
        else:
            print(f"  No books found in {specific_library.name}.")
    except Library.DoesNotExist:
        print(f"  Library '{library_name}' not found.")

    print("\n--- Query: Librarian for 'Community Read Library' ---")
    try:
        library_name = "Community Read Library"
        specific_library = Library.objects.get(name=library_name)
        librarian_for_library = specific_library.librarian
        print(f"  The librarian for {specific_library.name} is {librarian_for_library.name}.")
    except Library.DoesNotExist:
        print(f"  Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"  No librarian found for {specific_library.name}.")

if __name__ == '__main__':
    run_queries()