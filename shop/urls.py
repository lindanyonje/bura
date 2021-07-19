from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
from shop.views import CategoryDelete, CategoryUpdate, CategoryList,CategoryDetail ,CategoryCreate
from shop.views import SellerDelete, SellerUpdate, SellerList, SellerDetail,SellerCreate
from shop.views import ProductDelete, ProductUpdate,ProductList, ProductDetail,ProductCreate
from shop.views import OfferDelete, OfferUpdate, OfferList, OfferDetail,OfferCreate
from shop.views import VoucherDelete, VoucherUpdate,VoucherList, VoucherDetail,VoucherCreate
from shop.views import OrderDelete, OrderUpdate,OrderList, OrderDetail,OrderCreate
from shop.views import PaymentDelete, PaymentUpdate,PaymentList, PaymentDetail,PaymentCreate
from shop.views import CustomerDelete, CustomerUpdate,CustomerList, CustomerDetail,CustomerCreate

# you can use * to import all views instead of importing each one

urlpatterns=[
    path('', views.home, name="home"),
    path('categories/',CategoryList.as_view(),name="Category_List"),
    path('category/detail/<pk>',CategoryDetail.as_view(),name= 'category_detail'),
    path('create/category', CategoryCreate.as_view(),name= 'category_create'),
    path('update/category/<pk>/',CategoryUpdate.as_view(),name='category_update'),
    path('delete/category/<pk>/',CategoryDelete.as_view(),name='category_delete'),
    path('sellers/',SellerList.as_view(),name="Sellers"),
    path('seller/detail/<pk>',SellerDetail.as_view(),name= 'Seller_detail'),
    path('create/seller', SellerCreate.as_view(),name= 'Seller_create'),
    path('update/seller/<pk>/',SellerUpdate.as_view(),name='Seller_update'),
    path('delete/seller/<pk>/',SellerDelete.as_view(),name='Seller_delete'),
    path('products/',ProductList.as_view(),name="Product"),
    path('product/detail/<pk>',ProductDetail.as_view(),name= 'product_detail'),
    path('create/product', ProductCreate.as_view(),name= 'Product_create'),
    path('update/Product/<pk>/',ProductUpdate.as_view(),name='product_update'),
    path('delete/Product/<pk>/',ProductDelete.as_view(),name='Product_delete'),
    path('offers/',OfferList.as_view(),name="Offer"),
    path('offer/detail/<pk>',OfferDetail.as_view(),name= 'Offer_detail'),
    path('create/offer', OfferCreate.as_view(),name= 'Offer_create'),
    path('update/offer/<pk>/',OfferUpdate.as_view(),name='Offer_update'),
    path('delete/offer/<pk>/',OfferDelete.as_view(),name='Offer_delete'),
    path('vouchers/',VoucherList.as_view(),name="Voucher"),
    path('voucher/detail/<pk>',VoucherDetail.as_view(),name= 'Voucher_detail'),
    path('create/voucher', VoucherCreate.as_view(),name= 'Voucher_create'),
    path('update/voucher/<pk>/',VoucherUpdate.as_view(),name='Voucher_update'),
    path('delete/voucher/<pk>/',VoucherDelete.as_view(),name='Voucher_delete'),
    path('orders/',OrderList.as_view(),name="Order"),
    path('order/detail/<pk>',OrderDetail.as_view(),name= 'Order_detail'),
    path('create/order', OrderCreate.as_view(),name= 'Order_create'),
    path('update/order/<pk>/',OrderUpdate.as_view(),name='Order_update'),
    path('delete/order/<pk>/',OrderDelete.as_view(),name='Order_delete'),
    path('payments/',PaymentList.as_view(),name="Payment"),
    path('payment/detail/<pk>',PaymentDetail.as_view(),name= 'Payment_detail'),
    path('create/payment', PaymentCreate.as_view(),name= 'Payment_create'),
    path('update/payment/<pk>/',PaymentUpdate.as_view(),name='Payment_update'),
    path('delete/payment/<pk>/',PaymentDelete.as_view(),name='Payment_delete'),
    path('customers/',CustomerList.as_view(),name="Customer"),
    path('customer/detail/<pk>',CustomerDetail.as_view(),name= 'Customer_detail'),
    path('create/customer', CustomerCreate.as_view(),name= 'Customer_create'),
    path('update/customer/<pk>/',CustomerUpdate.as_view(),name='Customer_update'),
    path('delete/customer/<pk>/',CustomerDelete.as_view(),name='Customer_delete'),
    path('ajax/delete/category',views.deleteCategory,name="ajax_delete_category"),
    path('ajax/delete/Seller',views.deleteSeller,name="ajax_delete_seller"),
    path('ajax/delete/product',views.deleteProduct,name="ajax_delete_product"),


    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)