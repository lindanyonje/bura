from django.db.models.fields import Field
from django.http.response import JsonResponse
from django.shortcuts import render
from.models import Category, Seller, Product, Offer, Voucher, Order, Payment,Customer
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse
from django.http import JsonResponse
from django .contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    context = {}


    context['products'] = Product.objects.all()[:3]
    context['categories'] = Category.objects.all()

    return render(request, 'shop/frontend/home.html', context)

def adminDashboard(request):

    ##Declaring a dictionary used to package the data we shall
    ##send to the frontend html template for display.

    context = {}

    context['product_count'] =  Product.objects.all().count()
    context['order_count'] =  Order.objects.all().count()
    context['payment_count'] =  Payment.objects.all().count()
    context['payments'] =  Payment.objects.all()[:10]
    context['pending_orders'] =  Order.objects.filter(status ="Pending")



    return render(request, 'shop/admin/dashboard.html', context)



class CategoryList(ListView):
    
    login_required= True
    model = Category
    template_name= "shop/admin/category_list.html"

class CategoryDetail(DetailView):

    model = Category

class CategoryCreate(CreateView):  

    login_required= True
    model = Category
    template_name= "shop/admin/category_form.html"

    #specify the fields to be displayed

    fields = '__all__'

    #function to redirect user

    def get_success_url(self):
        return reverse('Category_List') #uses the path name

class CategoryUpdate(UpdateView):

    login_required= True
    model = Category
    fields = '__all__'
    template_name= "shop/admin/category_form.html"
    success_url = '/categories' #this uses the path url

class CategoryDelete(DeleteView):

    login_required= True
    model = Category
    success_url = '/categories'

    

class ProductList(ListView):

    login_required= True
    model =Product
    template_name= "shop/admin/product_list.html"

class ProductDetail(DetailView):

    login_required= True
    model = Product
    template_name= "shop/admin/product_detail.html"


class ProductCreate(CreateView): 

    login_required= True 
    model = Product
    template_name= "shop/admin/product_form.html"
    success_url = '/categories'

    #specify the fields to be displayed

    fields = '__all__'

    #function to ridirect user

    def get_success_url(self):
        return reverse('Product')

class ProductUpdate(UpdateView):

    login_required= True
    model = Product
    fields = '__all__'
    success_url = '/products'
    template_name= "shop/admin/product_form.html"


class ProductDelete(DeleteView):

    login_required= True
    model = Product
    success_url = '/products'
    template_name= "shop/admin/product_confirm_delete.html"



class  SellerList(ListView):

    login_required= True
    model =  Seller
    template_name= "shop/admin/seller_list.html"

class  SellerDetail(DetailView):

    login_required= True
    model =  Seller
    template_name= "shop/admin/seller_details.html"

class  SellerCreate(CreateView): 

    login_required= True 
    model =  Seller
    template_name= "shop/admin/seller_form.html"

    #specify the fields to be displayed

    fields ='__all__'

    #function to ridirect user

    def get_success_url(self):
        return reverse('seller_list')

class SellerUpdate(UpdateView):

    login_required= True
    model = Seller
    fields = ['name'] 
    template_name= "shop/admin/seller_form.html"
    success_url = '/sellers'

class  SellerDelete(DeleteView):

    login_required= True
    model =  Seller
    template_name= "shop/admin/seller_form.html"
    success_url = '/sellers'

    

class OfferList(ListView):

    login_required= True
    model = Offer
    template_name= "shop/admin/offer_list.html"

class OfferDetail(DetailView):

    login_required= True
    model = Offer

class OfferCreate(CreateView):  

    login_required= True
    model = Offer
    template_name= "shop/admin/offer_form.html"

    #specify the fields to be displayed

    fields = '__all__'

    #function to ridirect user

    def get_success_url(self):
        return reverse('offer_list')

class OfferUpdate(UpdateView):

    login_required= True
    model = Offer
    fields = '__all__'
    template_name= "shop/admin/offer_form.html"
    success_url = '/offers'

class OfferDelete(DeleteView):

    login_required= True
    model = Offer
    success_url = '/offers'  



class VoucherList(ListView):

    login_required= True
    model = Voucher
    template_name= "shop/admin/voucher_list.html"

class VoucherDetail(DetailView):

    login_required= True
    model = Voucher

class VoucherCreate(CreateView):

    login_required= True  
    model = Voucher
    template_name= "shop/admin/voucher_form.html"
    success_url = '/vouchers'

    #specify the fields to be displayed

    fields = '__all__'

    #function to ridirect user

    def get_success_url(self):
        return reverse('voucher_list')

class VoucherUpdate(UpdateView):

    
    login_required= Truemodel = Voucher
    fields = '__all__' 
    template_name= "shop/admin/voucher_form.html"
    success_url = '/offers'

class VoucherDelete(DeleteView):

    login_required= True
    model = Voucher
    success_url = '/vouchers'  




class OrderList(ListView):

    login_required= True
    model =Order
    template_name= "shop/admin/order_list.html"

class OrderDetail(DetailView):

    login_required= True
    model = Order
    template_name= "shop/admin/order_form.html"

class OrderCreate(CreateView): 

    login_required= True 
    model = Order
    template_name= "shop/admin/order_form.html"
    success_url = '/orders'


    #specify the fields to be displayed

    fields = '__all__'

    #function to ridirect user

    def get_success_url(self):
        return reverse('order_list')

class OrderUpdate(UpdateView):

    login_required= True
    model = Order
    fields = '__all__'
    template_name= "shop/admin/order_form.html"
    success_url = '/orders'

class OrderDelete(DeleteView):

    login_required= True
    model = Order
    template_name= "shop/admin/order_form.html"
    success_url = '/orders'  



class PaymentList(ListView):

    login_required= True
    model =Payment
    template_name= "shop/admin/payment_list.html"

class PaymentDetail(DetailView):

    login_required= True
    model = Payment

class PaymentCreate(CreateView):

    login_required= True  
    model = Payment
    template_name= "shop/admin/payment_form.html"
    success_url = '/payments'


    #specify the fields to be displayed

    fields = ['order_id', 'amount', 'description', 'invoice_number']

    #function to ridirect user

    def get_success_url(self):
        return reverse('payment_list')

class PaymentUpdate(UpdateView):

    login_required= True
    model = Payment
    fields = '__all__'
    template_name= "shop/admin/payment_form.html"
    success_url = '/payments'

class PaymentDelete(DeleteView):

    login_required= True
    model =Payment
    success_url = '/payments'  



class CustomerList(ListView):

    login_required= True
    model = Customer
    template_name= "shop/admin/customer_list.html"

class CustomerDetail(DetailView):

    login_required= True
    model =  Customer
    template_name= "shop/admin/customer_details.html"


class  CustomerCreate(CreateView):  

    login_required= True
    model =  Customer
    fields=' __all__'
    template_name= "shop/admin/customer_form.html"

    #specify the fields to be displayed

    #function to ridirect user

    def get_success_url(self):
        return reverse('customer_list')

class CustomerUpdate(UpdateView):

    login_required= True
    model =  Customer
    fields = '__all__'
    template_name= "shop/admin/customer_form.html"
    success_url = '/customers'

class CustomerDelete(DeleteView):

    login_required= True
    model =Customer
    template_name= "shop/admin/customer_confirm_delete.html"
    success_url = '/customers'

@login_required

def deleteCategory(request):
    Category_id= request.POST.get('id',None)
    category=Category.objects.get(id= Category_id)
    category.delete()
    data= {
        'deleted':True
    }
    return JsonResponse(data)


def deleteSeller(request):
    Seller_id= request.POST.get('id',None)
    seller=Seller.objects.get(id= Seller_id)
    seller.delete()
    data= {
        'deleted':True
    }

    return  JsonResponse(data)

def deleteProduct(request):

    Product_id= request.POST.get('id',None)
    product=Product.objects.get(id=Product_id)
    product.delete()
    data= {
        'deleted':True
    }

    return JsonResponse(data)