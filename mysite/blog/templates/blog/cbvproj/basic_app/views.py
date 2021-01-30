from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolList(ListView):
    context_object_name = 'school_list'
    model = models.School


class SchoolDetail(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreate(CreateView):
    fields = ('name', 'principal', 'locations')
    model = models.School

class SchoolUpdate(UpdateView):
    fields = ('name', 'principal', 'locations')
    model = models.School

class SchoolDelete(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
