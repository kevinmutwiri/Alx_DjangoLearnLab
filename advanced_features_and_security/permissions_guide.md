# Django Permissions and Groups Setup Guide

This document outlines the configuration of custom permissions and their enforcement using Django's built-in groups and permission system.

---

## 1. Custom Permissions Definition

Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) are defined within the `Meta` class of the `Book` model in `bookshelf/models.py`.  
These permissions are automatically registered with Django when migrations are applied.

---

## 2. Group Setup and Permission Assignment (Via Django Admin)

### Access Django Admin

After running migrations, log in to the Django admin interface at `/admin/`.

### Navigate to Groups

- Go to **"Groups"** under the **"Authentication and Authorization"** section.

### Create Groups and Assign Permissions

#### Editors
- Create a group named **"Editors"**.
- Assign the following permissions:
  - `Can create book` (bookshelf | book | can create book)
  - `Can edit book` (bookshelf | book | can edit book)

#### Viewers
- Create a group named **"Viewers"**.
- Assign the following permission:
  - `Can view book` (bookshelf | book | can view book)

#### Admins
- Create a group named **"Admins"**.
- Assign all four custom permissions:
  - `Can view book`
  - `Can create book`
  - `Can edit book`
  - `Can delete book`
- **Note**: Superusers automatically have all permissions.

### Assign Users to Groups

1. Navigate to **"Users"** under **"Authentication and Authorization"**.
2. Select or create a user.
3. In the user detail page, under **"Permissions"**, add the user to the appropriate group(s) (e.g., "Editors", "Viewers", "Admins").

---

## 3. Permission Enforcement in Views

In `bookshelf/views.py`, access control is enforced using Django’s class-based mixins:

- `LoginRequiredMixin`
- `PermissionRequiredMixin`

### View-Level Permissions

- `BookListView`: Requires `bookshelf.can_view` permission.
- `BookCreateView`: Requires `bookshelf.can_create` permission.
- `BookUpdateView`: Requires `bookshelf.can_edit` permission.
- `BookDeleteView`: Requires `bookshelf.can_delete` permission.

If a user lacks the required permission, a `PermissionDenied` exception (HTTP 403 Forbidden) is raised due to `raise_exception = True`.

---

## 4. Testing Permissions

To verify the setup, follow these steps:

### Create Test Users

- `viewer_user`: Assign to **"Viewers"**
- `editor_user`: Assign to **"Editors"**
- `admin_user`: Assign to **"Admins"**

### Test User Capabilities

Log in as each user and attempt the following:

- **Access book list**: `/books/`
- **Create a book**: `/books/add/`
- **Edit an existing book**: `/books/<pk>/edit/`
- **Delete an existing book**: `/books/<pk>/delete/`

### Expected Behavior

- **viewer_user**: Can only view the book list.
- **editor_user**: Can view, create, and edit books.
- **admin_user**: Can perform all actions.

---
