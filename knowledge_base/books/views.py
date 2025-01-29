from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
