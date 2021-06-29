from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    phone_number=models.IntegerField(null= True, blank= True)
    email=models.CharField(max_length=100, null=False, blank=False)
    password=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class CustomerAddress(models.Model):
    customer_id=models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    address=models.TextField(null=False, blank=False)
    pin=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Seller(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    email=models.CharField(max_length=100, null=False, blank=False)
    phone_number=models.IntegerField(null= True, blank= True)
    business_number=models.IntegerField(null= True, blank= True)
    status=models.CharField(max_length=100, null=False, blank=False)
    external_url=models.CharField(max_length=100, null=False, blank=False)
    password=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    email=models.CharField(max_length=100, null=False, blank=False)
    phone_number=models.IntegerField(null= True, blank= True)
    password=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    parent_id=models.ForeignKey('category',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    cost=models.IntegerField(null= True, blank= True)
    quantity=models.IntegerField(null= True, blank= True)
    description=models.TextField(null=False, blank=False)
    image=models.CharField(max_length=100, null=False, blank=False)
    featured=models.BooleanField(default=False)
    status=models.CharField(max_length=100, null=False, blank=False)
    category_id=models.ForeignKey('category',on_delete=models.CASCADE,blank=True,null=True)
    seller_id=models.ForeignKey('seller',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)



class Feedback(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    message=models.TextField(null=False, blank=False)
    email=models.CharField(max_length=100, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    rating= models.IntegerField(null=False, blank=False) 
    review=models.TextField( null=True, blank=True)
    customer_id=models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey('product',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    total=models.IntegerField(null= True, blank= True)
    status=models.CharField(max_length=100, null=False, blank=False, default="Pending")
    shipping_cost=models.IntegerField(null= True, blank= True)
    order_number=models.CharField(max_length=100, null=False, blank=False)
    Customer_id=models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    order_id= models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    quantity=models.IntegerField(null= False, blank= True) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True) 

class Payment(models.Model):
    order_id= models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    amount=models.IntegerField(null= True, blank= True)
    description=models.TextField(null=True, blank=True)
    invoice_number=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    order_id= models.ForeignKey('order',on_delete=models.CASCADE,blank=True,null=True)
    customer_address_id=models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    product_id= models.ForeignKey('product',on_delete=models.CASCADE,blank=True,null=True)  
    customer_id= models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
  

class Offer(models.Model):
    product_id= models.ForeignKey('product',on_delete=models.CASCADE,blank=True,null=True)  
    offer_amount=models.IntegerField(null=False, blank=False) 
    start_date=models.DateTimeField(null=False, blank=False)
    end_date=models.DateTimeField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Voucher(models.Model):
    product_id= models.ForeignKey('product',on_delete=models.CASCADE,blank=True,null=True)  
    voucher_amount=models.IntegerField(null= False, blank= False)
    voucher_tag=models.CharField(max_length=100, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
  



  

















