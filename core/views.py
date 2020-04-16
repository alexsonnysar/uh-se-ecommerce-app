from django.http import HttpResponse
from django.views.generic import ListView

from .models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'core/home.html'


