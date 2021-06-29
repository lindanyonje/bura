from django.shortcuts import render
from.models import Category, Seller, Product
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse

# Create your views here.

class CategoryList(ListView):

    model = Category

class CategoryDetail(DetailView):

    model = Category

class CategoryCreate(CreateView):  
    model = Category

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('category_list')

class CategoryUpdate(UpdateView):

    model = Category
    fields = ['name'] 
    success_url = '/categories'

class CategoryDelete(DeleteView):

    model = Category
    success_url = '/categories'

    

class ProductList(ListView):

    model =Product

class ProductDetail(DetailView):

    model = Product

class ProductCreate(CreateView):  
    model = Product

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('Product_list')

class ProductUpdate(UpdateView):

    model = Product
    fields = ['name'] 
    success_url = '/products'

class ProductDelete(DeleteView):

    model = Product
    success_url = '/products'


class  SellerList(ListView):

    model =  Seller

class  SellerDetail(DetailView):

    model =  Seller

class  SellerCreate(CreateView):  
    model =  Seller

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('category_list')

class SellerUpdate(UpdateView):

    model = Seller
    fields = ['name'] 
    success_url = '/sellers'

class  SellerDelete(DeleteView):

    model =  Seller
    success_url = '/sellers'

    



        
