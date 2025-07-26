from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser # Import CustomUser from the same models.py

# Register your models here.

# Define a custom Admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
    list_per_page = 25

# Register the Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)

# Custom Admin interface for the CustomUser model
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'date_of_birth', 'profile_photo')}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_of_birth')

# Register your CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
