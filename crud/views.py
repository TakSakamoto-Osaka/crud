from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    #親クラスのメソッドを実行
        context['name'] = "侍太郎"          #新しいデータを追加

        return context


class ProductListView(ListView):
    model = Product
    # template_name = "list.html"
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')


class ProductDetailView(DetailView):
    model = Product
    