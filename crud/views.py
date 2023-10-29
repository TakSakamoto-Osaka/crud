from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    # template_name = "list.html"
    paginate_by = 3
   
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'