# Retrieve Operation

> [home](./README.md)

**Command**:

```
from bookshelf.models import Book
book_retrieved = Book.objects.get(title="1984")
print(f"Title: {book_retrieved.title}")
print(f"Author: {book_retrieved.author}")
print(f"Publication Year: {book_retrieved.publication_year}")
```

**Expected Output**:

```
Title: 1984
Author: George Orwell
Publication Year: 1949
```