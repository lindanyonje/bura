from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Seller)
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Wishlist)
admin.site.register(Offer)
admin.site.register(Voucher)