from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Item

# Create your views here.

class Index(ListView):
    model = Item
    fields = '__all__'
