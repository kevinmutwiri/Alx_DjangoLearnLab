from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'profile_photo',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']