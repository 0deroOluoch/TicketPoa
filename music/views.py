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
from . models import Music





class MusicListView(ListView):
    model = Music
    template_name = 'music/home.html'
    context_object_name = 'musics'
    ordering = ['-date_posted']
    paginate_by = 8

class MusicDetalView(DetailView):
    model = Music
    
class MusicCreateView(CreateView):
    model = Music
    fields = ['Music_name','Music_descroption','start_date','end_date']

    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class MusicUpdateView(UpdateView):
    model = Music
    fields = ['Music_name','Music_descroption','start_date','end_date']


    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

class MusicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Music
    success_url = '/music'

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

#these will be implemented once the user module is in place, and permissions are set correctly. 




  
