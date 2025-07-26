# Django Shell CRUD Operations for Book Model

> [home](./README.md)

**This document details the commands and expected output**s for Create, Retrieve, Update, and Delete operations on the Book model within the Django shell.

## 1. Create Operation

**Python Command**:

```
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```

**Expected Output**:

```
<Book: 1984 by George Orwell (1949)>
```

**Comment**: This output confirms the successful creation of the Book instance and its string representation.

## 2. Retrieve Operation

**Python Command**:

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

**Comment**: This output shows the details of the retrieved book, confirming its attributes.

## 3. Update Operation

**Python Command**:

```
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)
```

**Expected Output**:

```
Nineteen Eighty-Four
```

**Comment**: This output confirms that the title of the book has been successfully updated.

## 4. Delete Operation

**Python Command**:

```
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print(Book.objects.all())
```

**Expected Output**:

```
<QuerySet []>
```

**Comment**: This output confirms the successful deletion of the book instance, as the queryset is now empty.