# Delete Operation

> [home](./README.md)

**Command**:

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