from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

def checkout(request):
    return render(request, 'checkout-page.html')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


