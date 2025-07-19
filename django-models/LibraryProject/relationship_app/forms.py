from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']