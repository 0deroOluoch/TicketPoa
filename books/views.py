from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View 
from xhtml2pdf import pisa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . models import Book





class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'Books'
    ordering = ['-date_posted']
    paginate_by = 8

class BookDetalView(DetailView):
    model = Book
    
class BookCreateView(CreateView):
    model = Book
    fields = ['Book_name','Book_descroption','start_date','end_date']

    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    fields = ['Book_name','Book_descroption','start_date','end_date']


    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/books'

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

#these will be implemented once the user module is in place, and permissions are set correctly. 




  
