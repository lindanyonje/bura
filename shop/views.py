from django.shortcuts import render
from.models import Category, Seller, Product, Offer, Voucher, Order, Payment,Customer
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'shop/frontend/home.html')

class CategoryList(ListView):

    model = Category
    template_name= "shop/admin/category_list.html"

class CategoryDetail(DetailView):

    model = Category

class CategoryCreate(CreateView):  
    model = Category
    template_name= "shop/admin/category_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('category_list')

class CategoryUpdate(UpdateView):

    model = Category
    fields = ['name'] 
    template_name= "shop/admin/category_form.html"
    success_url = '/categories'

class CategoryDelete(DeleteView):

    model = Category
    success_url = '/categories'

    

class ProductList(ListView):

    model =Product
    template_name= "shop/admin/product_list.html"

class ProductDetail(DetailView):

    model = Product

class ProductCreate(CreateView):  
    model = Product

    #specify the fields to be displayed

    fields = ['name']
    template_name= "shop/admin/product_list.html"

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
    template_name= "shop/admin/seller_list.html"

class  SellerDetail(DetailView):

    model =  Seller

class  SellerCreate(CreateView):  
    model =  Seller
    template_name= "shop/admin/seller_list.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('seller_list')

class SellerUpdate(UpdateView):

    model = Seller
    fields = ['name'] 
    template_name= "shop/admin/seller_form.html"
    success_url = '/sellers'

class  SellerDelete(DeleteView):

    model =  Seller
    success_url = '/sellers'

    

class OfferList(ListView):

    model = Offer
    template_name= "shop/admin/offer_list.html"

class OfferDetail(DetailView):

    model = Offer

class OfferCreate(CreateView):  
    model = Offer
    template_name= "shop/admin/offer_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('offer_list')

class OfferUpdate(UpdateView):

    model = Offer
    fields = ['name'] 
    template_name= "shop/admin/offer_form.html"
    success_url = '/offers'

class OfferDelete(DeleteView):

    model = Offer
    success_url = '/offers'  



class VoucherList(ListView):

    model = Voucher
    template_name= "shop/admin/voucher_list.html"

class VoucherDetail(DetailView):

    model = Voucher

class VoucherCreate(CreateView):  
    model = Voucher
    template_name= "shop/admin/voucher_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('voucher_list')

class VoucherUpdate(UpdateView):

    model = Voucher
    fields = ['name'] 
    template_name= "shop/admin/voucher_form.html"
    success_url = '/offers'

class VoucherDelete(DeleteView):

    model = Voucher
    success_url = '/vouchers'  




class OrderList(ListView):

    model =Order
    template_name= "shop/admin/order_list.html"

class OrderDetail(DetailView):

    model = Order

class OrderCreate(CreateView):  
    model = Order
    template_name= "shop/admin/oder_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('order_list')

class OrderUpdate(UpdateView):

    model = Order
    fields = ['name'] 
    template_name= "shop/admin/order_form.html"
    success_url = '/oders'

class OrderDelete(DeleteView):

    model = Order
    success_url = '/orders'  



class PaymentList(ListView):

    model =Payment
    template_name= "shop/admin/payment_list.html"

class PaymentDetail(DetailView):

    model = Payment

class PaymentCreate(CreateView):  
    model = Payment
    template_name= "shop/admin/payment_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('payment_list')

class PaymentUpdate(UpdateView):

    model = Payment
    fields = ['name'] 
    template_name= "shop/admin/payment_form.html"
    success_url = '/oders'

class PaymentDelete(DeleteView):

    model =Payment
    success_url = '/payments'  



class CustomerList(ListView):

    model = Customer
    template_name= "shop/admin/customer_list.html"

class CustomerDetail(DetailView):

    model =  Customer

class  CustomerCreate(CreateView):  
    model =  Customer
    template_name= "shop/admin/customer_form.html"

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('customer_list')

class CustomerUpdate(UpdateView):

    model =  Customer
    fields = ['name'] 
    template_name= "shop/admin/customer_form.html"
    success_url = '/customers'

class CustomerDelete(DeleteView):

    model =Customer
    success_url = '/customers'  




        
