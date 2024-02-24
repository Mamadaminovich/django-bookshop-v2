from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book-create.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book-update.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'book-details.html'
    context_object_name = 'book'
    
    