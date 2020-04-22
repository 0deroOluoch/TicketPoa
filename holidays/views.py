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
from . models import Holiday





class HolidayListView(ListView):
    model = Holiday
    template_name = 'holidays/home.html'
    context_object_name = 'holidays'
    ordering = ['-date_posted']
    paginate_by = 8

class HolidayDetalView(DetailView):
    model = Holiday
    
class HolidayCreateView(CreateView):
    model = Holiday
    fields = ['Destination_name','Holiday_descroption','start_date','end_date']

    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class HolidayUpdateView(UpdateView):
    model = Holiday
    fields = ['Destination_name','Holiday_descroption','start_date','end_date']


    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

class HolidayDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Holiday
    success_url = '/holidays'

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False






  
