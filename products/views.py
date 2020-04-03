from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'products/home.html'