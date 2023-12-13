from django.shortcuts import render
from .models import Estudiante
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class EstudianteListView(ListView):
    model = Estudiante

class EstudianteDetailView(DetailView):
    model = Estudiante
  

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = '__all__'
    success_url = reverse_lazy('home')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = '__all__'
    success_url = reverse_lazy('home')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("home")