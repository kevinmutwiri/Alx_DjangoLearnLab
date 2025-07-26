from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book

class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permission_required = 'bookshelf.can_view'
    raise_exception = True

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year', 'user']
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'
    raise_exception = True

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year', 'user']
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_edit'
    raise_exception = True

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_delete'
    raise_exception = True
