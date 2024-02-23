from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from crud.models import Product
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from crud.forms.search_form import SearchForm


class TopView(TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    #親クラスのメソッドを実行
        context['name'] = "侍太郎"          #新しいデータを追加

        return context


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    # template_name = "list.html"
    paginate_by = 3


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    #fields = ['name', 'price']
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'].fields['name'].widget.attrs["class"] = "input-name"
        context['form'].fields['name'].widget.attrs = {"class":"input-name", "placeholder":"商品名", "value":"ビデオ"}
       
        # context['form_search'] = SearchForm(...)
        
        return context

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')
    
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'



class SearchFormView(FormView):
    template_name = 'search.html'
    success_url = reverse_lazy('top')
    form_class = SearchForm
    